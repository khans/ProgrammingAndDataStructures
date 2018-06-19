'''
A simple class designed for a room object, where a room has an id or a unique number, 
the room has capacity(integer), the room has storage(integer) and the room has a situation(string).
The situation can be "Available", "InUse", Cleaning Up", "Not Clean"

'''
class Room():
    roomCost = 10       #Constant base value for a room
    strCost = 2         #Constant base value for storage
    partial = 'No'
    
    def __init__(self,id,number,capacity,storage,situation):
        self.id = id
        self.number = number
        self.capacity = capacity
        self.storage = storage
        self.situation = situation
        self.currAvSpace = capacity
        self.currAvStr = storage
        
    def showRoomInfo(self):
        return "Room number %d has %d person(s) to host and %d storage." % (self.number, self.capacity, self.storage)
    
    # method will return the tuple which is number of people and storage items assigned to the room
    '''
    if after assigning a customer we still have a bed available, this means the room is partially available
    Note: The room is partially available only if it has a bed for a person to sleep. 
    '''
    def assign(self,assignPpl, assignStr):
        # Capacity and Storage has to be >= requested
        # If the room will be shared then the remaining Capacity and storage has to be >= requested
        roomStatus = 'Not Reserved';
        if (self.currAvSpace >= assignPpl and self.currAvStr >= assignStr and self.situation == 'Available'):
            self.currAvSpace = self.capacity - assignPpl;
            self.currAvStr = self.storage - assignStr;
            
            # No bed left
            if (self.currAvSpace == 0):
                self.situation = "InUse";
            roomStatus = 'Reserved'
        dRoom = {}
        dRoom[self.id] = {self.number:roomStatus}
        return dRoom        
            
        
            
    # method returns current capacity = total capacity - assigned capacity
    def availPerson(self,assigned):
        if (assigned < 0 or assigned > self.capacity):
            return -1
        else:
            # availability = Room's Capacity - number of people assigned to the room 
            avail = self.capacity - assigned
            return avail                    
    # returns current storage = total storage - assigned storage
    def availStorage(self,assigned):
        if (assigned < 0 or assigned > self.storage):
            return -1
        else:
            # available Storage = Room's Storage - number of storage items already present in Rooms's Storage 
            avail = self.storage - assigned 
            return avail
        
    ''' Returns the room number requested if available    
    else returns error -1 for unavailable or -99 for out of bounds
    '''
    def isAvailable(self, reqPpl, reqStr, existPpl, existStr):
        #reqPpl: Number of people customer has requested a room for
        #reqStr: Number of storage items requested by Customer/Customer's family
        #existPpl: Number of people who are already in the room
        #existStr = Number of items already in the storage of the room
        unavailable = -1
        outOfBounds = -99
        if (self.capacity >= reqPpl and self.storage >= reqStr):
            if (self.availPerson(existPpl) >= reqPpl and self.availStorage(existStr) >= reqStr and self.situation =='Available'):
                return self.number
            return unavailable
        return outOfBounds
            

'''
usedRoom is a Room that has been used and guests have checked out. It is not clean so we 
need to ask the Gnome Squad to clean it
roomId: The room number
numPpl: number of people who occupied that room
checkedOut: The last checked out time, so that the room is empty
'''

class UsedRoom(Room):
    def __init__(self,id,roomId,numPpl,checkedOut):
        self.id = id
        self.roomId = roomId
        self.checkedOut = checkedOut
        self.numPpl = numPpl          


'''
room1 sleeps 2 people and has 1 storage space
room2 room sleeps 2 people and has 0 storage space
room3 room has 2 storage spaces and sleeps 1 person
room4 room sleeps ONE person and has ZERO storage space
'''
room1 = Room(1,1,2,1,"Available")
exists = room1.assign(1,1) #(1,1), 1 existPpl and 1 existStr
print(exists)
print (room1.availPerson(exists[0]))
print (room1.availStorage(exists[1]))
print(room1.isAvailable(1,0,exists[0],exists[1]))

room2 = Room(2,2,2,0, "Available" )
room3= Room(3,3,1,2, "Available")
room4 = Room(4,4,1,0, "Available")

u = UsedRoom(1,2,1,"2017-05-07 12:05")
print (u.checkedOut)


#InUseRoom is derived class - a type of Room that has occupants.
#It can be used only if it has a remaining bed. 
#If there is no bed but some storage, that room cannot be used 

class InUseRoom(Room):
    def __init__(self,id,roomId,numPpl,lastCheckIn,lastCheckOut):
        self.id = id
        self.roomId = roomId
        self.numPpl = numPpl
        self.lastCheckIn = lastCheckIn
        self.lastCheckOut = lastCheckOut 
    


