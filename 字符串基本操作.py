#字符串拼接，字符串重复：
>>> 'hello'+'world'
'helloworld'
>>> 'hello'+' world'
'hello world'
>>> ('hello'+' world') *4
'hello worldhello worldhello worldhello world'
>>> 'bvb'+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> 'bvb'+"3"
'bvb3'
>>> print"*"*8+'hello'+"*"*8
********hello********

>>> myjob='hacker'
>>> for c in myjob: print(c)
... 
h
a
c
k
e
r
>>> myjob='hacker'


>>> for k in myjob: print(k, end='')


hacker

>>> for k in myjob: print(k, end=' ')


h a c k e r 

>>> for k in myjob: print(k, end='-')


h-a-c-k-e-r-
>>> k in myjob
True
