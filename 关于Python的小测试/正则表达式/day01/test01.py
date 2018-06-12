# coding=UTF-8
import re
str="imooc python"
'''
pa=re.compile(r"iMooc", re.I)
ma=pa.match(str)
print(ma.group())
print(ma.span())

pa=re.compile(r"(imooc)", re.I)
ma=pa.match(str)
print(ma.groups())#groups()以组的形式来返回
'''
ma=re.match(r"..",str)  #
print(ma.group())



