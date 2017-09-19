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
				if s.isEmpty:
					balance = False
					break
				else:
					opens = "([{"
					closes = ")]}"
					top = s.pop()
					if not (opens.index[top] == closes.index[symbolString[i]]):
						balance = False
						break
		i += 1
	if balance and s.isEmpty:
		return True
	else:
		return False
