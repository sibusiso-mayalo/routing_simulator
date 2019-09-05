class Node:

    def __init__(self, nodeID=str(), nodeType=str() ):
        self.ID=nodeID
        self.type=self.set_type(nodeType)
        self.edges=dict()

    def set_type(self, new_type):
        self.type = new_type

    def add_edge(self, destination, cost, delay, rel_type):
        temp_list = list()
        temp_list.append(cost)
        temp_list.append(delay)

        self.set_type(rel_type)
        self.edges[destination] = temp_list
