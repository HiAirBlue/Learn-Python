"""栈描述及相关应用

	parChecker(symbolString) 括号匹配
	baseConverter(decNum, base) 十进制到N进制转换
	infixToPostfix(infixexpr)  中缀表达式转为后缀表达式
	postfixEval(postfixExpr)  后缀表达式求值
	"""

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

# 算法三  中缀表达式转为后缀表达式
def infixToPostfix(infixexpr):
	"""将中缀表达式转换为后缀表达式。

	输入的中缀表达式每个字符间要以空格分开。"""

	prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}  #用字典保存符号的优先级
	opStack = Stack()
	postfixlist = []
	tokenlist = infixexpr.split()
	#print("t3:",tokenlist)

	for token in tokenlist:
		#print('t4:',token)
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			postfixlist.append(token)
			#print('t1:',postfixlist)
		elif token == "(":
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != "(":
				postfixlist.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
				postfixlist.append(opStack.pop())
			opStack.push(token)
			#print('t2',opStack.peek())

	while not opStack.isEmpty():
		postfixlist.append(opStack.pop())
		
	return " ".join(postfixlist)
	
#算法四  求后缀表达式的值
def postfixEval(postfixExpr):
	"""求后缀表达式的值

	输入的后缀表达式字符间必须带有空格"""
	operandStock = Stack()
	tokenlist = postfixExpr.split()

	for token in tokenlist:
		try:
			num = int(token)
			operandStock.push(num)
		except ValueError:
			if token in "+-*/":
				operand2 = operandStock.pop()
				operand1 = operandStock.pop()

				if token == "+":
					result = operand1 + operand2
				elif token == "-":
					result = operand1 - operand2
				elif token == "*":
					result = operand1 * operand2
				elif token == "/":
					result = operand1 / operand2

				operandStock.push(result)

	return operandStock.pop()			



