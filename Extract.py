from Node import *
import json, sys
class Extract:

    def __init__(self, fileName):
        self.nodes = list()
        self.fileName = fileName

    def extractData(self):
        try:
            with open(self.fileName) as fileObj:
                for lines in fileObj:
                    contents = lines.split(",")

                    if len(contents) == 2:
                        self.nodes.append(Node(contents[0], contents[1]))
                    else:
						source = str(contents[0])
						destination = str(contents[1])
						rel_type = str(contents[2])
						cost = str(contents[3])
						delay = str(contents[4])
						
						tempNode =None
						for x in self.nodes:
							if x.ID == source: 
								tempNode = x
								break
							
						tempNode.populateNode(destination, rel_type, cost,delay)                            
                                   			 		
        except IOError as error:
            return "Could not read file:\n" + error
        else:
            return "success"
            
    def initialize(self):
    	array = dict()
        array["Edges"]= list()
        array["Rel-Type"] = list()
        array["ForwardTable"] = list()
        
        return array

    def get_JSON_data(self):
        collated= list()
        final_data = self.initialize()

        for node in self.nodes:
            #Add edged
            list_edges = list()
            for nextHop, data in node.edges.items():
                final_data["Edges"].append({"link":nextHop, "cost":data[0], "delay":data[1]})

            #Add Relation Types
            for linkID, relType in node.relType.items():
                final_data["Rel-Type"].append({"link":linkID, "type": relType})

            #Add fprwarding tables:
            for destNode, nextHop in node.forwardTable.items():
                final_data["ForwardTable"].append({"destination":destNode, "nextHop": nextHop})

            collated.append([node.ID, final_data])
            final_data = self.initialize()

        jsonData = json.dumps(collated,indent=4)
        print jsonData
        with open(self.fileName.split(".")[0]+".json","w") as file:
        	file.write(jsonData)


if __name__ == "__main__":
    app = Extract("testFile.txt")
    app.extractData()
    app.get_JSON_data()

    """with open("testFile.json") as json_file:
        data = json.load(json_file)
        print data[0]"""









