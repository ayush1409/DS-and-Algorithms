
class Node(object):

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

	def insert(self, data):
		if data < self.data:
			if not self.leftChild:
				self.leftChild = Node(data)
			else:
				self.leftChild.insert(data)
		else:
			if not self.rightChild:
				self.rightChild = Node(data)
			else:
				self.rightChild.insert(data)

	def remove(self, data, parentNode):

		if data < self.data:
			if self.leftChild:
				self.leftChild.remove(self, self)
			else:
				self.leftChild = Node(data)

		elif data > self.data:
			if self.rightChild:
				self.rightChild.remove(data, self)
			else:
				self.rightChild = Node(data)

		else:
			if self.leftChild is not None and self.rightChild is not None:
				self.data = self.rightChild.getMin()
				self.rightChild.remove(data, self)

			elif parentNode.leftChild == self:
				if self.leftChild:
					tempNode = self.leftChild
				else:
					tempNode = self.rightChild
				parentNode.leftChild = tempNode

			elif parentNode.rightChild == self:
				if self.rightChild:
					tempNode = self.rightChild
				else:
					tempNode = self.leftChild
				parentNode.rightChild = tempNode

	def getMin(self):
		if self.leftChild:
			self.leftChild.getMin()

	def getMax(self):
		if self.rightChild:
			self.rightChild.getMax()

	def InorderTraverse(self):
		if self.leftChild:
			self.leftChild.InorderTraverse()
		print(self.data)
		if self.rightChild:
			self.rightChild.InorderTraverse()
