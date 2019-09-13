import unittest
from RunGraph import *
from Node import *
class TestDeletion(unittest.TestCase):

    def test_delete(self):
        #Node to be deleted
        node = Node('ASN1','')

        #Manual deletion of a node
        extractObject = Extract('testFile.txt')
        del extractObject.nodes[node.ID]
        nodes = [items for items in extractObject.nodes].sort()

        #Deletion as the application would
        self.graph = RunGraph('testFile.txt')
        self.graph.remove_node(node)
        self.assertEqual([x for x in self.graph.nodes].sort(), nodes)

if __name__ == '__main__':
    #run test
    unittest.main()
