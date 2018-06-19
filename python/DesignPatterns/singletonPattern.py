class Singleton:
    __instance = None
    
    def __init(self):
      if self.__instance != None:
        raise ValueError("An instantiation already exists!")
    @classmethod    
    def getInstance(cls):
      if cls.__instance == None:
        cls.__instance = Singleton()
      return cls.__instance
      

p = Singleton()

x = Singleton.getInstance()
print(x)
y = Singleton.getInstance()
print(y)