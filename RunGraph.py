from Node import *
from Graph import *
class RunGraph:

    def __init__(self, filename='testFile.txt'):
        self.filename = filename
        self.nodes = dict()
        self.extractData()

    def extractData(self):
        try:
            with open(self.filename) as fileObj:
                for lines in fileObj:
                    contents = lines.split(",")
                    if len(contents) == 2:
                        self.nodes[contents[0]] = Node(contents[0], contents[1])
                    elif len(contents) > 2:
                        source = str(contents[0])
                        destination = str(contents[1])
                        rel_type = str(contents[2])
                        cost = str(contents[3])
                        delay = str(contents[4])

                        for existingNode in self.nodes.values():
                            if existingNode.ID == source:
                                existingNode.add_edge(destination, cost, delay, rel_type)
                    else:
                        pass
        except IOError as error:
            return "Could not read file:\n" + error
        else:
            return "success"

if __name__ == '__main__':
    print('Extracting data.....\n')
    run = RunGraph()
    calculate_obj = Graph(run.nodes)

    total_cost = 0
    path = str()

    while True:
        print('Nodes : ')
        for node in run.nodes.keys():
            print(node)

        start = raw_input('\nEnter starting node: ')
        dest = raw_input('\nenter destination node: ')

        print('Calculating path......\n')
        start = run.nodes[start]
        dest = run.nodes[dest]

        came_from, cost = calculate_obj.calculate_path(start, dest)
        path = calculate_obj.reconstruct_path(came_from, start,dest)

        is_path_valid = calculate_obj.validate_rules(path)
        if is_path_valid:
            print('Path : ', path)
            print('Cost : ', cost[path[-1]])
            quit = raw_input('Exit ? Y/N\n')
            if quit =='Y':
                break
        else:
            print is_path_valid
