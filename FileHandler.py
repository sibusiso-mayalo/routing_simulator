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
                    contents = lines.strip().split(",")

                    if contents[0]=='': #empty line
                        pass
                    elif len(contents) ==2 or len(contents)==5:
                        #2 indicates node+type, 4 indicates src,dest,cost,delay
                        pass
                    else:
                        validation_status = False
                        break
        else:
            validation_status = False
        return validation_status

if __name__ == "__main__":
    test = FileHandler('testFile.txt')
    print(test.validate_file())
