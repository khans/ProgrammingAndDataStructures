from datetime import datetime as dt, timedelta as td
import sys
'''
A simple class designed for a room object, where a room has an id or a unique number, 
the room has capacity(integer), the room has storage(integer) and the room has a situation(string).
The situation can be "Available", "Occupied", Cleaning Up", "Not Clean"

'''
class Room():
    roomCost = 10.0       #Constant base value for a room
    strCost = 2.0         #Constant base value for storage
    
    def __init__(self,id,number,capacity,storage,situation):
        self.id = id
        self.number = number
        self.capacity = capacity
        self.storage = storage
        self.situation = situation
        
        '''
        currAvSpace is the current Capacity of the room, if the room is occupied by one person, then it wll be updated to
        capacity of the room - 1.
        Similarly currAvStr is the current available storage in the room. 
        This is updated if the room has storage items or is cleared of storage
        '''
        self.currAvSpace = capacity     
        self.currAvStr = storage
        
    def showRoomInfo(self):
        return "Room number %d has %d person(s) to host and %d storage." % (self.number, self.capacity, self.storage)
    
    '''
    method assign() will return a dictionary.
    Input is the number of people to host and number of storage items to store.
    Returns a dictionary of the form {roomId :{roomNumber:{roomSituation:roomStatus}}}.
    Example: {1: {1: {'Available': 'Reserved'}}}, so the room is available and is reserved for the guest.
    If it does not go as expected then the room is not reserved.
    An incorrect reservation where we request more poeple to host than the room's capacity will 
    return something like: {1: {1: {'Available': 'Not Reserved'}}}, which means the room is available
    but not reserved for the guest.
    '''
    
    def assign(self,assignPpl, assignStr):
        # If the room will be shared then the remaining capacity and storage has to be >= requested
        roomStatus = 'Not Reserved';
        if (self.currAvSpace >= assignPpl and self.currAvStr >= assignStr and self.situation == "Available"):
            self.currAvSpace = self.capacity - assignPpl;
            self.currAvStr = self.storage - assignStr;
            
            roomStatus = "Reserved"
        
        dRoom = {}
        dRoom['RoomId'] = self.id
        dRoom['RoomNumber'] = self.number
        dRoom['RoomSituation'] = self.situation
        dRoom['RoomStatus'] = roomStatus
        
        return dRoom 
    
    # This function will change the situation of the room to "Not Clean"
    # since it has just been vacated
    def freeRoom(self):
        self.currAvSpace = self.capacity
        self.currAvStr = self.storage
        self.situation = "Not Clean"
    
    def changeSituation(self,situation):
        self.situation = situation
        
        
            
        


'''
InUseRoom is derived class - a type of Room that has occupants.
It can be used only if it has a remaining bed. 
If there is no bed but some storage, that room cannot be used 
'''


class InUseRoom(Room):
    def __init__(self,id,roomId,numPpl,lastCheckIn,lastCheckOut):
        self.id = id
        self.roomId = roomId
        self.numPpl = numPpl
        self.lastCheckIn = dt.strptime(lastCheckIn, "%Y-%m-%d %H:%M")
        self.lastCheckOut = dt.strptime(lastCheckOut, "%Y-%m-%d %H:%M") 
        self.situation = "Occupied"
  


#Following can be uncommented and saved, then on command line run 'python room.py' to see the objects created

'''
r = Room(7,7,2,2,"Available")               #Room instance example
print("The Room object's parameters are:")
print('Id = ' + str(r.id))
print('Room Number = ' + str(r.number))
print('Room Capacity = ' + str(r.capacity))
print('Room Storage = ' + str(r.storage))
print('Room Situation = ' + r.situation)

ir = InUseRoom(7,7,2,"2017-06-04 12:05","2017-06-06 12:05")  #UsedRoom Instance example
print("The InUseRoom object's parameters are:")
print('InUseRoom Id = ' + str(ir.id))
print('InUseRoom roomId = ' + str(ir.roomId))
print('InUseRoom Number of occupants = ' + str(ir.numPpl))
print('InUseRoom last Check In = ' + str(ir.lastCheckIn))
print('InUseRoom last Check Out = ' + str(ir.lastCheckOut))
print('InUseRoom Situation = ' + ir.situation)
'''



