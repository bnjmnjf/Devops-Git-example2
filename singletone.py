class ConfigValues:
    
    __instance=None
    
    @staticmethod
    def getInstance():
        if ConfigValues.__instance==None:
            ConfigValues()
        return ConfigValues.__instance
    
    def __init__(self):
        if ConfigValues.__instance != None:
            raise Exception("This clas is a singletone!")
        else:
            ConfigValues.__instance=self
            
s=ConfigValues.getInstance()
print(s)


s=ConfigValues.getInstance()
print(s)


s = ConfigValues()