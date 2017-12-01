>>> items = ['aaa', 111, (4,5),2.01]
>>> tests = [(4,5),3,14]
>>> for key in tests:
...     for item in items:
...             if key == item:
...                     print(key,'was found')
...                     break

#替代方案：
for key in tests:
    if key in items:
        print(key,'was found')
    else:
        print(key, 'was not found')



>>> seq1='spam'
>>> seq2='scam'
>>> res=[]
>>> for x in seq1:
...     if x in seq2:
...             res.append(x)
...
>>> res
['s', 'a', 'm']
