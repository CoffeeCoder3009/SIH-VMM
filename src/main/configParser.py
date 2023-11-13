
import datetime

class Parser:
    # """
    #     The Parser parses the config files of .hwk extension
    #     A sample .hwk file written as

    #             @This is a comment

    #             date-created = 2023-11-4 23:40:15
    #             last-modified =  2023-11-4 23:50:15
    #             home-directory = C:\Users\Asus\Downloads\ARM_Build


    #             config-file=a.hwk
    #             project-name = First_Project
    #             directories=[mag-res,abc]
    #             mag-res=[abe.txt,abx.csv,ab.png]
        
    #         - The lines starting with @ represent a comment
    #         - There are two types of configurations stored 
    #             1. Value-Key Pairs:  They have a label and a respective value associated
    #             2. Directory: 
    #                 2.1. The directory stored in the config file must be at the end of the file
    #                 2.2. The label 'directories' will contain the list of directories created
    #                 2.3. Then each directory is called on with a list following containing the list of files in it

    #     parse is a static function. It reads the the file with the path given in the
    #     argument. It return a tuple containing two dictionaries. 
    #     The first dictionary  contains the value key pairs and the second one contain the directories.
    
    # #TODO: Why does this ''' giving  SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 274-275: truncated \UXXXXXXXX escape
    # """
   

    def __init__(self,path):
        #TODO: Add the constructor
        self.path=path
        return
    

    def is_parseable(self):
        #TODO: implement parseability checker
        return True

    def parse(self):
        
        '''
        path is the path of the .hwk file
        It parses the file and return a tuple of two dictionaries containing value-key pairs and directory
        '''



        #TODO: Refractor

        f = open(self.path,"r")
        token={}
        directories={}
        if f.readable():
            line = f.readline().strip()
            text=""
            nLine = 0
            while line:
                if line.find("directories")!=-1:
                    break
                nLine+=1
                text+=line
                if line[0]!="@" and not line.isspace():
                    content = line.strip(" \n\t").split("=")
                    token[content[0].strip()]=content[1].strip()
                line = f.readline()

                
            while line:
                if line.find("directories")!=-1:
                    j = line.find('[')
                    k = line.find(']')
                    dirs = line[j+1:k].split(',')
                    for i in dirs:
                        directories[i]=None
                    break
                line = f.readline()
            while line:
                for i in directories.keys():
                    if line.find(i)!=-1:
                        j = line.find('[')
                        k = line.find(']') 
                        dirs = line[j+1:k].split(',')
                        directories[i]=dirs
                        break
                line=f.readline()

        f.close()
        
        return token,directories
    






