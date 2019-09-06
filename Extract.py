from Node import *
import json, sys
class Extract:

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

"""
    def convert(self, source, dest):
    	temp_list = dict()
    	temp_list["source"] = source
    	temp_list["target"]= dest
    	return temp_list

    def get_JSON_data(self):
    	node_list = list()
    	for node in self.nodes:
    		node_list.append(node.getInfo())

    	temp = dict()
        temp["nodes"] = node_list
        temp["links"] = self.edges

        nodes = json.dumps(temp,indent=4)
        #edges = json.dumps(self.edges,indent=4)

        print nodes
        with open(self.fileName.split(".")[0]+".json","w") as file:

        	file.write(nodes)
if __name__ == "__main__":
    app = Extract("testFile.txt")
    app.extractData()
    app.get_JSON_data()

    """ """with open("testFile.json") as json_file:
        data = json.load(json_file)
        print data[0]"""
