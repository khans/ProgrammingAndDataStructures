from abc import ABCMeta, abstractmethod

# interface/abstractclass for command ICommand
class ICommand():
    __metaclass__ = ABCMeta
    @abstractmethod
    def execute(self):
        pass
    def unexecute(self):
        pass

# Concrete command that inherits the ICommand
# The constructor requires the instance of the Receiver class
class LightOn(ICommand):
    light = None
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def unexecute(self):
        self.light.off()
    


class LightOff(ICommand):
    light = None
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def unexecute(self):
        self.light.on()

class LightDim(ICommand):
    light = None
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.dim()
    def unexecute(self):
        self.light.up()

class LightUp(ICommand):
    light = None
    
    def __init__(self,light):
        self.light = light
    
    def execute(self):
        self.light.up()
    
    def unexecute(self):
        self.light.dim()
    
        
# Receiver
class Receiver():
    def on(self):
        print ("the light is ON!")
    
    def off(self):
        print("the light is OFF")

    def dim(self):
        print("the light is DIM")
    
    def up(self):
        print("the light is UP")
        
receiver = Receiver()
# Invokers (can be more than 1)
class Invoker():
    # Either use setCommand() or receive commands via the constructor
    # all are of type ICommand
    def __init__(self,lightOnC, lightOffC, lightDimC, lightUpC):
        self.commandOn = lightOnC
        self.commandOff = lightOffC
        self.commandDim = lightDimC
        self.commandUp = lightUpC
    
    def clickOn(self):
        self.commandOn.execute()
    
    def clickOff(self):
        self.commandOff.execute()
    
    def clickDim(self):
        self.commandDim.execute()
    
    def clickUp(self):
        self.commandUp.execute()
        
        

lon = LightOn(receiver)
loff = LightOff(receiver)
ldim = LightDim(receiver)
lup = LightUp(receiver)

i = Invoker(lon,loff,ldim,lup)
i.clickOn()
i.clickOff()
i.clickDim()
i.clickUp()

'''
the light is ON!
the light is OFF
the light is DIM
the light is UP
'''