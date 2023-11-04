import os

class Configuration:
    '''
    
    '''

    def __init__(self, config_file,project_name):
        self.config_file = config_file
        self.project_name = project_name


    def loader(self):

        try:
            if os.path.isfile(self.config_file):
                if self.config_file[-4:].lower()==".hwk":
                    #TODO: Implement the parser. Then add it here
                    pass
                else:
                    raise Exception("Invalid Configuration File")
        except:
            raise FileNotFoundError("Invalid Configuration File")
