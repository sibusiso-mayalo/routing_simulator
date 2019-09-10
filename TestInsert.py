import unittest
from RunGraph import *
from Node import *
class TestInsert(unittest.TestCase):

    def setUp(self):
        self.graph = RunGraph('testFile.txt')

    def get_nodes(self):
        return [nodes for nodes in self.graph.nodes][:] #shallow coppy

    def test_insert(self):
        #Add node manually
        new_node = Node('ASN100', 'T2')
        temp_nodes = self.get_nodes()
        temp_nodes.append(new_node.ID)

        #Add node like how the application would
        self.graph.add_node(new_node)
        self.assertEqual(temp_nodes.sort(),[nodes for nodes in self.graph.nodes].sort())

    def tearDown(self):
        self.graph = None

if __name__ == '__main__':
    unittest.main()
