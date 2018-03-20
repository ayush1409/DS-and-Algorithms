
from Node import Node

class AVL(object):

	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		parentNode = self.rootNode
		if not self.rootNode:
			parentNode = Node(data)
			self.rootNode = parentNode
		else:
			parentNode = self.rootNode.insert(data, self.rootNode)

		self.rebalance(parentNode)
#		self.height = 1 + max(self.rightChild.height, self.leftChild.height)
	def rebalance(self, Node):
		slope_x = Node.getSlope()

		if slope_x == 2:
			slope_y = self.leftChild.getSlope()
			if slope_y == -1:
				Node.leftChild = rotateLeft(Node.leftChild)
			Node.rightChild = rotateRight(Node)

		elif slope_x == -2:
			slope_y = self.rightChild.getSlope()
			if slope_y == 1:
				rotateRight(Node.leftChild)
			rotateLeft(Node)

	def getSlope(self):
		return self.leftChild.height - self.rightChild.height

	def rotateLeft(self, Node):
		y = Node.data
		z = Node.rightChild.data
		tll = Node.leftChild
		tlrl = Node.leftCHild.rightChild
		tlrr = Node.rightChild.rightChild

		Node.data = z
		Node.leftChild = Node.rightChild
		Node.leftChild.data = y
		Node.leftChild.leftChild = tll
		Node.leftChild.rightChild = tlrl
		Node.rightChild = tlrr
		return Node

	def rotateRight(self, Node):

		x = Node.data
		y = Node.leftChild.data
		tll = Node.leftChild.leftChild
		tlr = Node.leftChild.rightChild
		tr = Node.rightChild

		Node.value = y
		Node.rightChild = Node.leftChild
		Node.rightChild.data = x
		Node.leftChild = tll
		Node.rightChild.leftChild = tlr
		Node.rightChild.rightChild = tr
		return Node
