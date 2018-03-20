
class Node(object):

	def __init__(self, data, parentnode):
		self.data = data
		self.parentnode = parentnode
		self.rightChild = None
		self.leftChild = None
		self.balance = 0
		self.height = 0

	def insert(self, data, parentnode):
		if data < self.data:
			if not self.leftChild:
				self.leftChild = Node(data, parentnode)
			else:
				self.rightChild.insert(data, parentnode)

		return parentnode

	def InorderTraverse(self):
		if self.leftChild:
			self.leftChild.InorderTraverse()

		print(self.data)

		if self.rightChild:
			self.rightChild.InorderTraverse()

	def getMin(self):
		if not self.leftChild:
			return self.data
		else:
			self.leftChild.getMin()

	def getMax(self):
		if not self.rightChild:
			return self.data
		else:
			self.rightChild.getMax()
