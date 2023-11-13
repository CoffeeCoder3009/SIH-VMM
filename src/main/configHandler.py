import os
from configParser import Parser
import datetime

class Configuration:
    '''
    This class handlers the interaction with configuration file
    It has following functions
        -Generating config file with .hwk extension when a new project 
            is created
        -Updating the config file as userr changes anysetting or 
        .3
            configuration
        -Loading an already existing project
        -The saving and loading is done through a parser class 
            in configParser.py file  
    '''

    def __init__(self, config_file_path):
        self.config_path = config_file_path
        self.project_name = None
        self.config_file = None
        self.date_created = None
        self.last_modified = None
        self.home_directory = None
        self.out_dirs=[]
        self.out_files={}
        if self.config_path==None:
            self.loader(True)
        return


    def load(self,new=False):
        if not new:
            try:
                if os.path.isfile(self.config_path):
                    if self.config_path[-4:].lower()==".hwk":
                        #TODO: Implement the parser. Then add it here
                        parser = Parser(self.config_path)
                        if parser.is_parseable():
                            config,dirs = parser.parse()

                            self.update_config(config,dirs)

                        pass
                    else:
                        raise Exception("Invalid Configuration File")
            except:
                raise FileNotFoundError("Configuration File not found")
        else:
            #if the project doesn't exits the make a new project
            self.make_project()
    

    def make_project(self):
        #TODO: Craete this function to make new projects
        return

    def update_config(self,config=None,dirs=None,project_name=None):
        if config!=None:
            self.config_path = config['home-directory']+'/'+config['config-file']
            self.project_name = config['project-name']
            self.date_created = config['date-created']
            self.last_modified=str(datetime.datetime.today())
            self.config_file = config['config-file']
            self.home_directory = config['home-directory']
            self.out_dirs = ['directories']
            self.out_files = dirs
        else:
            date = str(datetime.datetime.today())
            if project_name:
                self.project_name = project_name
            self.date_created = date
            self.last_modified = date
            self.config_file = self.project_name + '.hwk'
            self.out_dirs = []
            self.out_files = {}
            
            if True:   
                #This is to make indentation block for localisation of variables
                path=''
                for i in self.config_path.split('/')[:-1]:
                    path+=i
                    path+='/'

                self.home_directory = path[:-1]
    
    def write(self):
        if self.writeable():
            f = open(self.config_file,'w')
            f.write('date-created = '+self.date_created+'\n')
            f.write('last-modified = '+self.last_modified+'\n')
            f.write('home-directory = '+self.home_directory+'\n')
            f.write('config-file = '+self.config_file+'\n')
            f.write('project-name = '+self.project_name+'\n')
            f.write('directories = '+str(self.out_dirs).replace("'","")+"\n")
            for i in self.out_files.keys:
                f.write(i+' = '+str(self.out_files[i]).replace("'","")+"\n")
            
            f.close()
            pass

    def writeable(self):
        #TODO: Complete this function
        return True
