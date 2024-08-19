import datetime

class NsLogger():
    '''
        Logger for Nsoporte, it needs filename and Appname
    '''
    def __init__(self,file_name:str = "/var/log/syslog",
                 app_name:str = None, 
                 docker:bool = False) -> None:
        self.file_name = file_name
        self.app_name = app_name 
        self.docker = docker

    @staticmethod
    def print_to_log(self,string:str,level:str = "info", quiet:str = False)->None:
        now = datetime.datetime.now()
        date_log =  now.strftime("%Y-%m-%d %H:%M:%S")      
        # Check for appname 
        if self.app_name == None:
            body = f"{date_log} [{level}] {string}"
        else:
            body = f"[{self.app_name}] {date_log} [{level}] {string}"    
        
        # Check for Docker mode 
        if self.docker == False:
            f = open(self.file_name, 'a+')
            f.write(f"{body}\n")
            f.close()

        if quiet == False:
            print(body,flush=True)

    
    def line(self,line:str,quiet:bool = False, level:str = "info")->None:
        '''     Print a line in the Logfile: \n
                line -> Line or text to print \n
                quiet -> If you need to print the message in the console or only in the file \n
                level = > Log Level (info, warning, error)
        '''
        self.print_to_log(self,
                          string=line,
                          quiet=quiet,
                          level=level)

    def dictionary(self,dicionary:dict,quiet:bool = False, level:str = "info", header:str = "Printing Dictionary") ->None:
        '''
            Print a Dictionary, key -> value format \n
            dictionary -> Dictionary to print \n
            quiet -> If you need to print the message in the console or only in the file \n
            level -> Log Level (info, warning, error) \n
            header -> Line Header to show
        '''
        msg = f"{header}\n"

        for key in dicionary:
            msg = f"{msg}\n {key} ====> {dicionary[key]}"

        msg = f"{msg}\n"
        self.print_to_log(self,
                          string=msg,
                          quiet=quiet,
                          level=level)
        
    def list(self,list:list,quiet:bool = False, level:str = "info", header:str = "Printing list") ->None:
        '''
            Print a List, id -> value format \n
            list -> List to print \n
            quiet -> If you need to print the message in the console or only in the file \n
            level -> Log Level (info, warning, error) \n
            header -> Line Header to show
        '''
        counter = 0
        msg = f"{header}\n"

        for item in list:
            msg = f"{msg}\n{counter} ===> {str(item)}"
            counter = counter + 1

        msg = f"{msg}\n"
        self.print_to_log(self,
                          string=msg,
                          quiet=quiet,
                          level=level)