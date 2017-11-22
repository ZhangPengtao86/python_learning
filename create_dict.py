REPODIR = '/home/build/repo'
KVM_DIR = '/home/build/kvm-build/nightly'
XEN_DIR = '/home/build/xen-build/nightly'
KVM_DATA = '/home/build/kvm-build/data'
XEN_DATA = '/home/build/xen-build/data'
PROXY = 'http://proxy-shz.intel.com:911'
URL = 'git://vt-sync.sh.intel.com'
KERNEL = 'git://vt-sync.sh.intel.com/linux-stable.git'
SERVER_URL_XEN = 'http://vmm-build.sh.intel.com/xen-build'
SERVER_URL_KVM = 'http://vmm-build.sh.intel.com/kvm-build'
LOCAL_URL = 'vt-sync'
DOMAIN_SH = '.sh.intel.com'
DOMAIN = '.intel.com'
KERNEL_URL = 'https://www.kernel.org/'


source = dict()
source['kvm'] = dict()
source['kvm']['repopath'] = REPODIR + '/kvm'
source['kvm']['url'] = URL + '/kvm.git'
source['kvm']['branch'] = 'next'
source['kvm']['build_tag'] = 0
source['ovmf'] = URL + '/edk2.git'
source['qemu'] = dict()
source['qemu']['repopath'] = REPODIR + '/qemu'
source['qemu']['url'] = URL + '/qemu.git'
source['qemu']['branch'] = 'master'
source['qemu']['build_tag'] = 0
source['xen'] = dict()
source['xen']['repopath'] = REPODIR + '/xen'
source['xen']['url'] = URL + '/xen.git'
source['xen']['branch'] = 'master'
source['xen']['build_tag'] = 0
source['dom0'] = dict()
source['dom0']['repopath'] = REPODIR + '/linux-stable'
source['dom0']['branch'] = 'master'
source['kernel_web'] = KERNEL_URL
source['pvgrub2'] = URL + '/grub.git'
