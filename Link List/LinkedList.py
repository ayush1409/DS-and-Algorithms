from Node import Node

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.counter = 0

	def insertAtStart(self, data):
		newNode = Node(data)

		if self.head:
			newNode.nextNode = self.head
			self.head = newNode
		else:
			self.head = newNode

		self.counter = self.counter + 1

	def insertAtEnd(self, data):
		newNode = Node(data)

		if self.head:
			tempNode = self.head
			while tempNode.nextNode is not None:
				tempNode = tempNode.nextNode

			tempNode.nextNode = newNode

		else:
			self.head = newNode

		self.counter = self.counter + 1

	def Traverse(self):
		tempNode = self.head
		while tempNode is not None:
			print(tempNode.data)
			tempNode = tempNode.nextNode

	def remove(self, data):
		if self.head:
			if data == self.head.data:
				self.head = self.head.nextNode
			else:
				self.head.remove(data, self.head)  # Note: this is the remove method from Node class

	def size(self):
		return self.counter
