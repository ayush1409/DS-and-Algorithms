from Node import Node

class BST(object):
	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		if not self.rootNode:
			self.rootNode = Node(data)
		else:
			self.rootNode.insert(data)

	def remove(self, dataToRemove):
		if self.rootNode.data == dataToRemove:
			tempNode = Node(None)
			tempNode.leftChild = self.rootNode
			self.rootNode.remove(dataToRemove, tempNode)
		else:
			self.rootNode.remove(dataToRemove, None)

	def getMax(self):
		if self.rootNode:
			return self.rootNode.getMac()

	def getMin(self):
		if rootNode:
			return self.rootNode.getMin()

	def Traverse(self):
		if self.rootNode:
			self.rootNode.InorderTraverse()
