"""利用递归实现一些算法
	
	1.利用递归求和 listsum(aList)

"""

# 算法一 利用递归求和
def listsum(aList):
	if len(aList) == 1:
		return aList[0]
	else:
		return aList[0] + listsum(aList[1:])


#算法二 进制转换
def toBase(n,base):
	convertString = '0123456789ABCDEF'
	if n < base:
		return convertString[n]
	else:
		return toBase(n//base,base) + convertString[n%base]
