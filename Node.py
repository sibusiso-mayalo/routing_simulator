class Node:

	def __init__(self, nodeID, nodeType):
		self.ID = nodeID
		self.type=nodeType
		self.edges = dict()
		self.relType = dict()
		self.forwardTable = dict()
		
	def populateNode(self, destinationNode, relType, cost, delay):
		self.edges[destinationNode] = (cost,delay)
		self.relType[destinationNode] = relType
		
	def update_fwdTable(self, destinationNode, nextHop):
		self.forwardTable[destinationNode] = nextHop
