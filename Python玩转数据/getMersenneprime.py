""" 该算法用于计算出梅森素数。

	梅森数是指形如2^n-1的数，如果一个梅森数是素数那么它称为梅森素数。当n为合数时， Mn一定为合数。但当n为素数时，Mn不一定皆为素数"""

import math

def getPri(min,max):
	"""返回min到max之间的素数"""
	priList = []

	for num in range(min,max+1):
		i = 2
		stillOk = True

		while i <= math.sqrt(num) and stillOk:
			if num % i == 0:
				stillOk = False
				break
			i += 1
		
		if stillOk:
			priList.append(num)

	return priList


def getMerPri(n = 6):
	"""返回梅森素数"""

	merPriDict = {}
	tmpList = []
	step = 2
	i = 0 

	while i < n:
		tmpList = getPri(step,step+20)

		for pri in tmpList:
			Mn = 2**pri - 1
			if getPri(Mn, Mn) != []:
				i += 1
				merPriDict[pri] = Mn
				if i >= n:
					break

		step += 20
	
	return merPriDict



