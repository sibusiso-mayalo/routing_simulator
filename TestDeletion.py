import unittest
from RunGraph import *
from Node import *
class TestDeletion(unittest.TestCase):

    def setUp(self, node='ASN1', filename='testFile.txt'):
        self.filename = filename
        self.graph = RunGraph('testFile.txt')
        self.list = self.get_node_list()
        self.to_be_removed = Node(node, '')

    def get_node_list(self):
        #return sorted list of nodes
        return [node for node in self.graph.nodes].sort()[:]

    def test_delete(self):
        #all nodes
        extractObject = Extract(self.filename)

        #deleting node as the application would
        extractObject.remove_node(self.to_be_removed)
        nodes = [items for items in extractObject.nodes]

        self.list.remove(self.to_be_removed.ID)
        self.assertEqual(self.list, nodes.sort())

    def tearDown(self):
        self.graph=None

if __name__ == '__main__':
    #run test
    unittest.main()
