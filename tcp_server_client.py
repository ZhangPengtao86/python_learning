[root@skl-s home]# cat tcp_server.py 
#!/usr/bin/python

from socket import *

from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from: ', addr

	while True:
		data = tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		tcpCliSock.send('[%s] %s' % (ctime(), data))
	tcpCliSock.close()
tcpCliSock.close()


[root@vt-master ~]$ cat tcp_client.py
#!/usr/bin/python

from socket import *
HOST = '192.168.98.179'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
        data = raw_input('> ')
        if not data:
                break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
                break
        print data
tcpCliSock.close()

