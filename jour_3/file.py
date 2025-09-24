class File:

    def __init__(self,file_name):
        print("init")
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        print("File entering")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("File exitting...")
        if(self.file is None or self.file.closed): return 
        self.file.close()
    
    def ouvrir(self,mode):
        print("File openning...")
        self.file = open(self.file_name,mode,encoding="utf-8")

    def ecrire(self,chaine):
        print("ecrire")
        if(self.file is None or self.file.closed): return 
        self.file.write(chaine)
    
    def __del__(self):
        print("File closing...")
        if(self.file is None or self.file.closed): return 
        self.file.close()


