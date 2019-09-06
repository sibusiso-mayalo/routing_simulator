from Conversions import *
from PriorityQueue import *
class Graph:

    def __init__(self, nodes = dict()):
        self.nodes = nodes

    def calculate_path(self, start_node, destination_node):
        #A* Search Algorithm
        frontier = PriorityQueue()
        frontier.put(start_node, 0)

        came_from = dict()
        came_from[start_node] = None

        cost_so_far = dict()
        cost_so_far[start_node.ID] = 0

        while not frontier.empty():
            current_node = frontier.get()

            if current_node.ID == destination_node.ID: #handle this equality
                break

            for next_node_id, next_node_values in current_node.edges.iteritems():
                new_cost = cost_so_far[current_node.ID] + int(next_node_values[0])#total cost

                if next_node_id not in cost_so_far or new_cost < cost_so_far[next_node_id]:
                    cost_so_far[self.nodes[next_node_id].ID] = new_cost
                    priority = new_cost + self.heuristic(destination_node, self.nodes[next_node_id])
                    frontier.put(self.nodes[next_node_id], priority)
                    came_from[next_node_id] = current_node.ID

        return came_from, cost_so_far

    def heuristic(self, dest_node, current_node):
        #Calculate heuristic: cost so far + cost to dest
        estimate = 0
        for enum in Conversions:
            if dest_node.type == str(enum).split('.')[1]:
                estimate += enum.value
            if current_node.type == str(enum).split('.')[1]:
                estimate += enum.value
        return estimate

    def validate_rules(self, path_arr):
        forward = False
        len_array = len(path_arr)

        for i in range(1, len_array):
            current_node = self.nodes[path_arr[i-1]]
            next_node = self.nodes[path_arr[i]]

            if (i+1) == len_array:
                #This means that the 'next_node' is the target node
                forward = True
                break

            if current_node.type == 'P' or current_node.type =='IX':
                #check if the next node is the customer of the current link (P or IX)
                if next_node.type =='C' or next_node.type == 'PC':
                    forward = True
                else:
                    return 'RuleViolationError: From Node '+current_node.ID+' to Node '+next_node.ID
        return forward

    def reconstruct_path(self, came_from, start, goal):
        #Reverse the path found to start from source to destination node
        current= goal.ID
        path = []

        while current != start.ID:
            path.append(current)
            current= came_from[current]
        path.append(start.ID) # optional
        path.reverse() # optional
        return path
