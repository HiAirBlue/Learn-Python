"""队列的描述及相关算法
	1. 单向队列描述 Queue()
	2. 双向队列描述  Deque()
	3. 烫手山芋算法 hotpotato(namelist,num)
	4. 回文判断 palCheck(aString)

	"""

class Queue:

	"""队尾进，队首出单向队列"""
	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class Deque:
	"""双向队列，两头都可进可出"""
	def __init__(self):
		self.items = []

	def addFront(self,item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)




#算法一 烫手山芋，约瑟夫问题，一些人围成一个圈，顺次报数第num个的被踢出，求最后剩下的人。
def hotpotato(namelist,num):
	simqueue = Queue()

	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
		simqueue.dequeue()

	return simqueue.dequeue()


#算法二 利用双向队列进行会问检查
def palCheck(aString):
	cDeque = Deque()
	stillOk = True
	for ch in aString:
		cDeque.addFront(ch)

	while cDeque.size() > 1 and stillOk:
		if not cDeque.removeFront() == cDeque.removeRear():
			stillOk = False

	return stillOk
