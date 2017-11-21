#!/usr/bin/env python3.7
# env 程序可以通过系统的搜索路径的设置，来找到Python解释器的位置，这样的写法，代码更具有可以移植性！不需要把解释器的安装路径写死。
import sys
print(sys.platform)
print(2 ** 100)
x = 'Spam'
print(x * 8)


[root@skl-s ~]# python t1.py 
linux2
1267650600228229401496703205376
SpamSpamSpamSpamSpamSpamSpamSpam
