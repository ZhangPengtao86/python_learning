>>> D = { 'a':1, 'b':2, 'c':3, 'd':4}
>>> for k, v in D.items():
...     print(k, v)
...
a 1
b 2
c 3
d 4
>>> D.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#任何嵌套的序列都可以自动解包，并自动赋值
>>> T = [(('a','b'),'c'), (('d', 'e'),'f')]
>>> for ((x,y),z) in T:
...     print(x,y,z)
...
a b c
d e f
