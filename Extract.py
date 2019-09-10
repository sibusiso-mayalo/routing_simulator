from __future__ import print_function
from Node import *
import datetime
import json, sys
class Extract:

    def __init__(self, filename='testFile.txt'):
        self.filename = filename
        self.nodes = dict()
        self.extractData()
        self.write_to_json()

    def extractData(self):
        #extarct data from the nput file
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

    def add_node(self, node):
        self.nodes[node.ID] = node

    def remove_node(self, node):
        del self.nodes[node.ID]

    def write_to_json(self):
        #write data to a json file
        edges =list()
        nodes =list()

        for key_parent, parent_object in self.nodes.items():
            for key_link, value_link in parent_object.edges.items():
                edges.append(self.convert_edge(key_parent, key_link))
            nodes.append(self.convert_node(parent_object.type, key_parent))

        out=open("static/"+self.filename.split('.')[0]+".json","w")
        out.write(json.dumps({'links':edges, 'nodes':nodes}, indent=4))
        out.close()

    def convert_node(self, type, id):
        #clean node info
        temp_list = dict()
    	temp_list["id"] = id
    	temp_list["Type"]= type
    	return temp_list

    def convert_edge(self, source, dest):
        #clean link info
    	temp_list = dict()
    	temp_list["source"] = source
    	temp_list["target"]= dest
    	return temp_list

if __name__ == "__main__":
    app = Extract("testFile.txt")
