import zred
a=5
b=[5]	
data={}
data["a"]=a
data["b"]=b
def imp(m):
	print m
data["imp"]=imp
zred.zAPI("a in b imp('hola');p=2",data)