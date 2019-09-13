import unittest
from RunGraph import *
from Node import *
class TestCost(unittest.TestCase):

    def setUp(self):
        self.graph = RunGraph('testFile.txt')

    def get_nodes(self):
        return [nodes for nodes in self.graph.nodes][:] #shallow coppy

    def test_insert(self):
        #Specify start and destination node
        source, destination = 'ASN1','ASN5'

        results = self.graph.get_results(source, destination)
        self.assertEqual(results['cost'], 0)

    def tearDown(self):
        self.graph = None

if __name__ == '__main__':
    unittest.main()
