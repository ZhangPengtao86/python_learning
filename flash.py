#! /usr/bin/env python
# Copyright(c) 2017, Intel Corporation
#
# Redistribution  and  use  in source  and  binary  forms,  with  or  without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of  source code  must retain the  above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name  of Intel Corporation  nor the names of its contributors
#   may be used to  endorse or promote  products derived  from this  software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,  BUT NOT LIMITED TO,  THE
# IMPLIED WARRANTIES OF  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT  SHALL THE COPYRIGHT OWNER  OR CONTRIBUTORS BE
# LIABLE  FOR  ANY  DIRECT,  INDIRECT,  INCIDENTAL,  SPECIAL,  EXEMPLARY,  OR
# CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT  NOT LIMITED  TO,  PROCUREMENT  OF
# SUBSTITUTE GOODS OR SERVICES;  LOSS OF USE,  DATA, OR PROFITS;  OR BUSINESS
# INTERRUPTION)  HOWEVER CAUSED  AND ON ANY THEORY  OF LIABILITY,  WHETHER IN
# CONTRACT,  STRICT LIABILITY,  OR TORT  (INCLUDING NEGLIGENCE  OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,  EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import struct
import sys
import tempfile
import os
import subprocess
import fcntl
import filecmp
import stat
from array import *


def check_rpd(ifile):
    data = ifile.read(0x20)
    pof_hdr = struct.unpack('IIIIIIII', data)
    for i in range(0, 3):
        if pof_hdr[i] != 0xffffffff:
            print "invalid rpd file"
            sys.exit(1)

    if pof_hdr[3] != 0x6a6a6a6a:
        print "invalid rpd file"
        sys.exit(1)

    return pof_hdr[4]


def reverse_bits(x, n):
    result = 0
    for i in xrange(n):
        if (x >> i) & 1:
            result |= 1 << (n - 1 - i)
    return result


def reverse_bits_in_file(ifile, ofile):
    bit_rev = array('B')
    for i in range(0, 256):
        bit_rev.append(reverse_bits(i, 8))

    while True:
        ichunk = ifile.read(4096)
        if not ichunk:
            break

        ochunk = ''
        for b in ichunk:
            ochunk += chr(bit_rev[ord(b)])
        ofile.write(ochunk)


def get_flash_size(dev):

    MEMGETINFO = 0x80204d01

    try:
        fd = os.open(dev, os.O_SYNC | os.O_RDONLY)
    except Exception as e:
        print "failed to open " + dev + ": ", e
        sys.exit(1)

    ioctl_data = struct.pack('BIIIIIQ', 0, 0, 0, 0, 0, 0, 0)

    try:
        ret = fcntl.ioctl(fd, MEMGETINFO, ioctl_data)
    except Exception as e:
        print "ioctl failed: ", e
        sys.exit(1)

    ioctl_odata = struct.unpack_from('BIIIIIQ', ret)

    os.close(fd)

    return ioctl_odata[2]


def flash_erase(dev, start, nbytes):
    MEMERASE = 0x40084d02

    try:
        fd = os.open(dev, os.O_SYNC | os.O_RDWR)
    except Exception as e:
        print "failed to open " + dev + ": ", e
        sys.exit(1)

    ioctl_data = struct.pack('II', start, nbytes)

    try:
        ret = fcntl.ioctl(fd, MEMERASE, ioctl_data)
    except Exception as e:
        print "ioctl failed: ", e
        sys.exit(1)

    os.close(fd)


def flash_write(dev, start, nbytes, ifile):

    try:
        fd = os.open(dev, os.O_SYNC | os.O_RDWR)
    except Exception as e:
        print "failed to open " + dev + ": ", e
        sys.exit(1)

    os.lseek(fd, start, os.SEEK_SET)

    while nbytes > 0:
        if (nbytes > 4096):
            rbytes = 4096
        else:
            rbytes = nbytes

        ichunk = ifile.read(rbytes)

        if not ichunk:
            print "read of flash failed"
            sys.exit(1)

        os.write(fd, ichunk)
        nbytes -= rbytes

    os.close(fd)


def flash_read(dev, start, nbytes, ofile):
    try:
        fd = os.open(dev, os.O_SYNC | os.O_RDONLY)
    except Exception as e:
        print "failed to open " + dev + ": ", e
        sys.exit(1)

    os.lseek(fd, start, os.SEEK_SET)

    while nbytes > 0:
        if (nbytes > 4096):
            rbytes = 4096
        else:
            rbytes = nbytes

        ichunk = os.read(fd, rbytes)

        if not ichunk:
            print "read of flash failed"
            sys.exit(1)

        ofile.write(ichunk)
        nbytes -= rbytes

    os.close(fd)


def parse_args():
    descr = 'A tool to help update the flash used to configure an '
    descr += 'Intel FPGA at power up.'

    epi = 'example usage:\n\n'
    epi += '    fpgaflash user new_image.rpd /dev/mtd0\n\n'
    epi += 'Use the output of \'ls -l /sys/class/mtd\' to help determine\n'
    epi += 'which device, /dev/mtd*.\n\n'

    fc = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description=descr, epilog=epi,
                                     formatter_class=fc)

    parser.add_argument('type', help='type of flash programming',
                        choices=['user', 'factory_that_can_brick_board'])
    parser.add_argument('file', help='rpd file to program into flash')
    parser.add_argument('device',
                        help='mtd device to program (e.g. /dev/mtd0)')
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    try:
        mode = os.stat(args.device).st_mode
        if not stat.S_ISCHR(mode):
            print args.device, "is not a device file."
            sys.exit(1)

    except Exception as e:
        print "Couldn't stat", args.device, ":", e
        sys.exit(1)

    flash_size = get_flash_size(args.device)

    print "flash size is " + str(flash_size)

    try:
        ifile = open(args.file, 'rb')
    except Exception as e:
        print "open() failed:", e
        sys.exit(1)

    start_addr = check_rpd(ifile)

    ofile = tempfile.NamedTemporaryFile(mode='wb', delete=False)

    if args.type == 'factory_that_can_brick_board':
        msg = "Are you sure you want to perform a factory update? [Yes/No]"
        sys.stdout.write(msg)
        line = sys.stdin.readline()
        if line == "Yes\n":
            start_addr = 0
        else:
            sys.exit(1)

    ifile.seek(start_addr)

    print "reversing bits"
    reverse_bits_in_file(ifile, ofile)

    ifile.close()
    ofile.close()

    print "erasing flash"
    flash_erase(args.device, start_addr, (flash_size - start_addr))

    nbytes = os.path.getsize(ofile.name)
    try:
        rfile = open(ofile.name, 'rb')
    except Exception as e:
        print "open() failed:", e
        sys.exit(1)

    print "writing flash"
    flash_write(args.device, start_addr, nbytes, rfile)
    rfile.close()

    vfile = tempfile.NamedTemporaryFile(mode='wb', delete=False)

    print "reading back flash"
    flash_read(args.device, start_addr, nbytes, vfile)

    vfile.close()

    print "verifying flash"

    retval = filecmp.cmp(ofile.name, vfile.name)

    os.remove(ofile.name)
    os.remove(vfile.name)

    if retval:
        print "flash successfully verified"
    else:
        print "failed to verify flash"
        sys.exit(1)

