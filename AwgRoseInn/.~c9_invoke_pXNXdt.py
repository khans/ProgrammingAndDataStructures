class Room():
    def __init__(self,number,capacity,storage):
        self.number = number
        self.capacity = capacity
        self.storage = storage
        
    def showRoomInfo(self):
        print "Room number %d has %d people to host and %d storage." % (self.number, self.capacity, self.storage)
    
    def assign(self,assignPpl, assignStr):
        if (self.capacity >= assignPpl and self.storage >= assignStr):
            return (assignPpl, assignStr)
        else:
            return (-1,-1);
    
    def availPerson(self,assigned):
        if (assigned < 0 or assigned > self.capacity):
            return -1
        else:
            # availability = Room's Capacity - number of people assigned to the room 
            avail = self.storage - assigned
            return avail                    
    
    def availStorage(self,assigned):
        if (assigned < 0 or assigned > self.storage):
    def isAvailable(self, request):
        else:
            # available Storage = Room's Storage - number of storage items already present in Rooms's Storage 
            avail = self.storage - assigned 
            return avail
            
    def isAvailable(self, reqPpl, reqStr, existPpl, existStr):
        pass
        #reqPpl: Number of people customer has requested a room for
        #reqStr: Number of storage items requested by Customer/Customer's family
        #existPpl: Number of people who are already in the room
        #existStr = Number of items already in the storage of the room
        unavailable = -1
        outOfBounds = -99
        if (self.capacity >= reqPpl and self.storage >= reqStr):
            if (self.availPerson(existPpl) >= reqPpl and self.availStorage(existStr) >= reqStr):
                return (self.number, "Room " + self.number + " is available to accomodate the request!")
            return (unavailable, "Room " + self.number + " is unavailable to accomodate request at this time")
        return (outOfBounds,"Requested exceeds room's original capacity")
            
        




s = Room(3,6,5) 
s.showRoomInfo();