

class Stack:
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		"""返回栈顶元素，不修改栈"""
		return self.items[len(self.items)-1]

	def  isEmpty(self):
		return self.items == []
	
	def size(self):
		return len(self.items)


#算法一  符号匹配
def parChecker(symbolString):
	"""用于实现符号匹配"""

	s = Stack()
	balance = True
	i = 0
	while i < len(symbolString) and balance:
		if symbolString[i] in "([{)]}":
			if symbolString[i] in "([{":
				s.push(symbolString[i])
			else:
				if s.isEmpty():
					balance = False
					#print('t2:',balance,s.isEmpty())
					break
				else:
					opens = "([{"
					closes = ")]}"
					top = s.pop()
					print(top)
					if not opens.index(top) == closes.index(symbolString[i]):
						balance = False
						#print('t3',balance)
						break
		i += 1
		#print("i=",i)
	if balance and s.isEmpty():
		return True
	else:
		return False

#算法二  十进制到N进制转换

def baseConverter(decNum, base):
	"""用于十进制向n进制转换"""

	digits = "0123456789ABCDEF"
	s = Stack()

	while decNum > 0:
		rem = decNum % base
		s.push(rem)
		decNum = decNum // base

	newNum = ""
	while not s.isEmpty():
		newNum = newNum + digits[s.pop()]
	
	return newNum
