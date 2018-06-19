from datetime import datetime as dt, timedelta as td
import room
'''
This is a modue for the class Squad
every squad member can legally work for 8 hours a day.
A one gnome cleaning squad can legally work for 8*3600 seconds in a day.
Minimum cleaning time a gnome requires to clean a room is 3600 seconds.
'''
#In the following class a method is sending error codes
#I am assuming "-999" and "-1000" are error codes 

class Squad():
    maxSeconds = 8 * 3600       #maximum Seconds a gnome in a squad can legally work
    minCleanTime = 1 * 3600     #minimum Seconds required for a cleaning session
    
    def __init__(self,id, startTime,nextAvailable):      
        self.id = id
        self.startTime = dt.strptime(startTime, "%Y-%m-%d %H:%M")
        self.nextAvail = dt.strptime(nextAvailable, "%Y-%m-%d %H:%M")
     
    #Update the next availabilty of the gnome squad    
    def updateAvailability(self,nextAvailable):
        self.nextAvail = nextAvailable
        return
    
    
    '''
    Following method will be called to find out by what time a room will be clean. 
    Input: numPpl is number of people who were staying in the room
    This will return tdict a small dictionary with item Time and its value is a list
    The list first element is a message and second element is 
    either an error code or the time when the room is ready
    '''
    def timeEstimate(self,numPpl):
        #We will return tdict
        tdict = {}
        if numPpl < 0:
            tdict['Time'] = ["Room cannot be cleaned, incorrect request", "-1001"]
            return tdict
        #time in hours for a room
        timeToClean = (self.minCleanTime)/3600 + (0.5)*numPpl
        
        
        
        if(self.nextAvail is not None):
            finishTime = self.nextAvail + td(hours=timeToClean)
            
            diff = finishTime - self.startTime
            #Convert to seconds
            totalSec = diff.total_seconds()
            if (totalSec <= self.maxSeconds):       # should be less than <= 8
                tdict['Time'] = ["Room will be cleaned",str(finishTime)]
            else:
                tdict['Time'] = ["Room will not be cleaned", "-999"]
                
            ''' If after cleaning there is still time left 
            for some other cleaning session, then update the nextAvail of the squad
            '''
            if (totalSec <= (self.maxSeconds - self.minCleanTime)):
                self.updateAvailability(finishTime)
            else:
                self.updateAvailability(None)
        else:
            tdict['Time'] = ["Room will not be cleaned", "-1000"]
            
        
        
        return tdict
       
        
        

#Following can be uncommented and saved, then on command line run 'python squad.py' to see the objects created

a = dt.strptime("2017-06-07 12:05", "%Y-%m-%d %H:%M")
s = Squad(1, "2017-06-07 09:05","2017-06-07 09:05")
print("The Squad object's parameters are:")
print("Squad Id = " + str(s.id))
print("Squad's Start Time = " + str(s.startTime))
print("Squad's Next Availability = " + str(s.nextAvail))

s.updateAvailability(a)
print("Squad's Next Availability has been updated to = " + str(s.nextAvail))
print(s.timeEstimate(2))    # Answer: {'Time': ['Room will be cleaned', '2017-06-07 14:05:00']}













    
        
    