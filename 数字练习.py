#!/usr/bin/env python
-*- coding: utf-8 -*-
import random

>>> random.randint(1,9)
9
>>> random.randint(1,9)
7
>>> random.randint(1,9)
5
>>> random.random()
0.6572818554184239
>>> random.random()
0.7637729124740587
>>> random.choice([1,2,3,4])
1
>>> random.choice([1,2,3,4])
4
>>> random.choice([1,2,3,4])
3


>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(6)
2.449489742783178

#字符串操作：
>>> 'hello'
'hello'
>>> s = 'hello'
>>> s[0]
'h'
>>> s[1]
'e'
>>> len(s)
5
>>> s[-1]
'o'
>>> s[-2]
'l'
#下面两种方法等价
>>> s[len(s)-1]
'o'
>>> s[-1]
'o'
>>> s[0:3]
'hel'
>>> s[:3]
'hel'
>>> s[:-1]
'hell'
>>> s[:]
'hello'
>>> s + 'xyz'
'helloxyz'
>>> s * 8
'hellohellohellohellohellohellohellohello'
>>> s.find('ll')
2
>>> s.upper()
'HELLO'


#注意replace并不能改变字符串，只是生成了新的字符串对象罢了，因为字符串具有不可以变性。
>>> s.replace('he','xyz')
'xyzllo'
>>> s
'hello'

#split(), join()两个函数功能相反，注意分隔符的位置！！！
>>> l = '/root/tao'
>>> l.split('/')
['', 'root', 'tao']
>>> '/'.join(['', 'root', 'tao'])
'/root/tao'
>>> spl = l.split('/')
>>> '/'.join(spl)
'/root/tao'
>>> s.isalpha()
True
>>> line='aaa,bbb, ccc\n'
>>> line.rstrip()
'aaa,bbb, ccc'
>>> '%s eggs, and %s ' % ('spam', 'SPAM!')
'spam eggs, and SPAM! '
>>> '{} eggs, and {}'.format('spam', 'SPAM')
'spam eggs, and SPAM'


>>> dir(line)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


