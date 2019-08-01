class FileHandler:

    def __init__(self, fileName):
        self.fileName = str(fileName)
        self.extensions = ['csv','txt','xls']
        self.nodes = list()
        
    def get_fileExtension(self):
        return str(self.fileName.split('.')[1])
        
    def validate_file(self):
        #validate extenstion
        validation_status = True
  
        if self.get_fileExtension() in self.extensions:
            #read and validate for missing information
            with open(self.fileName) as fileObj:
                for lines in fileObj:
                    contents = lines.split(",")

                    source = str(contents[0])
                    destination = str(contents[1])
                    rel_type = str(contents[2])
                    cost = str(contents[3])
                    delay = str(contents[4])
                    
                    if (not source) or (not destination) or(not rel_type) or (not cost) or (not delay):
                        validation_status = False
                        break
                    else:
                        self.nodes.append(list(lines))
                    
                    
        else:
            validation_status = False
         
        return validation_status
            
if __name__ == "__main__":
    test = fileHandler('testFile.txt')
    print(test.validate_file())
        
