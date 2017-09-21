

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
	"""用于十进制向n进制转换

	原理基于连除基数，将取得余数装入堆栈，依次弹出"""

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


def infixToPostfix(infixexpr):
	"""将中序表达式转换为后序表达式。

	输入的中序表达式每个字符间要以空格分开。"""

	prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}  #用字典保存符号的优先级
	opStack = Stack()
	postfixlist = []
	tokenlist = infixexpr.split()

	for token in tokenlist:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			postfixlist.append(token)
		elif token == "(":
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != "(":
				postfixlist.append(topToken)
				topToken.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixlist.append(opStack.pop())
			opStack.push(token)

		while not opStack.isEmpty():
			postfixlist.append(opStack.pop())
		
		return " ".join(postfixlist)
				

