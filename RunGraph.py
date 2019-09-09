from Node import *
from Graph import *
from Extract import *
class RunGraph:

    def __init__(self, filename='testFile.txt'):
        self.filename = filename
        self.nodes = Extract(self.filename).nodes

    def get_results(self, src, dest):
        #This function takes a source and destination node adn calculate the path between them.
        calculate_obj = Graph(self.nodes)

        came_from, cost = calculate_obj.calculate_path(self.nodes[src],self.nodes[dest])
        path = calculate_obj.reconstruct_path(came_from, self.nodes[src], self.nodes[dest])#reverse the path

        is_path_valid = calculate_obj.validate_rules(path)#enforce validation rules
        final_data = dict()
        if is_path_valid:
            final_data['path'] = path
            final_data['cost'] =  cost[path[-1]]
            return final_data
        else:
            return is_path_valid
if __name__ == '__main__':
    run = RunGraph('testFile.txt')

    while True:
        source = raw_input("Enter start node: ")
        destination = raw_input("enter destination node: ")
        results = run.get_results(source, destination)

        if type(results) == 'str()':
            print results
        else:
            print 'Path is : ',results['path']
            print 'Cost is : ',results['cost']

        exit_code = raw_input('Exit? (Y / N): ')
        if exit_code == 'Y':
            break
