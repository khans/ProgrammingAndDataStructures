# Reference: https://www.youtube.com/watch?v=_BpmfnqjgzQ

from abc import ABCMeta, abstractmethod

# IObservable
class IWeatherStation():
    __metaclass__ = ABCMeta
    @abstractmethod
    def addDisplay(self,theDisplay):
        pass
    
    @abstractmethod
    def remDisplay(self,theDisplay):
        pass
    
    @abstractmethod
    def notify(self):
        pass

# IObservers
class IDisplay():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    #Scenario 1, push,pull
    def update(self):
        pass
    
    #Scenario 2, push,push
    '''
    def update(self,theStation):
        pass
    '''
    
# Concrete Observable    

class ConcreteWS(IWeatherStation):
    
    displays = set();
    temperature = None
    
    def addDisplay(self,theDisplay):
        self.displays.add(theDisplay)
    
    def remDisplay(self,theDisplay):
        self.displays.remove(theDisplay)
    
    def notify(self):
        #Scenario 1, push-pull
        for each in self.displays:
            each.update()
        
        #Scenario 2, push-push
        '''
        for each in self.displays:
            each.update(self)
        '''
        
    def getTemperature(self):
        return self.temperature
    
    def setTemperature(self, someTemp):
        self.temperature = someTemp
    
# Concrete Observer
class ConcreteD(IDisplay):
    
    #Needs to be instantiated with the Station in Scenario 1 (Push-pull)
    def __init__(self,theStation):
        self.theStation = theStation
        #self.theStation not required to be instantiated in push-push way
    
    
    def update(self):
        temp = self.theStation.getTemperature()
        print (temp)
        
    
    #Scenario 2, push-push
    '''    
    def update(self,theStation):
        theStation.getTemperature()
    '''

# Concrete Weather Station
ws = ConcreteWS();

# Concrete Displays
d1 = ConcreteD(ws)
d2 = ConcreteD(ws)

# Add Displays to Weather Station
ws.addDisplay(d1)
ws.addDisplay(d2)


ws.setTemperature(40)
ws.notify()

ws.setTemperature(100)
ws.notify()