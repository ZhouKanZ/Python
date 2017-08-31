#!usr/bin/env python3

# python3 高级特性　　

# 切片
# only list have this featrue , in python3 ,there have two class 
# list  such as : list and tuple  string is a kind of list as well;

# ex:

# 1. list 
L = ['Michael','Sarch','Tracy','Bob','Jack']
print(L[:3])

# 2.tuple 
# at frist I must reslove what is it named 'tuple', which looks like '(1,2,3)'
# ok just like list 

N = (1,2,3,4)
print(N[:2])

# there has a question when N[:1] , print a special tuple 
# (1,)

# 迭代　（Interator）
# as usual,we complete list interator using 'for ... in ...'
# such as java : 
# for(i = 0; i < list.length ; i++){
#	  list[i]
# }
# dict is similar to map in java , ps : it is disordered 

d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)

from collections import Iterable
a = isinstance('abc',Iterable)
b = isinstance([1,2,3],Iterable)
c = isinstance(123,Iterable)
print(a,b,c)

# True true false






