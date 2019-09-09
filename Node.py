class Node:

    def __init__(self, nodeID=str(), type=str() ):
        self.ID=nodeID
        self.type=type
        self.edges=dict()

    def add_edge(self, destination, cost, delay, rel_type):
        temp_list = list()
        temp_list.append(cost)
        temp_list.append(delay)
        temp_list.append(rel_type)

        self.edges[destination] = temp_list
