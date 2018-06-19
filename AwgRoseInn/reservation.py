from datetime import datetime as dt
import customer, room

class Reservation():
    def __init__(self,id,roomId,custId,checkIn,checkOut,reqPpl,reqStr):
        self.id = id
        self.roomId = roomId
        self.custId = custId
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.reqPpl = reqPpl
        self.reqStr = reqStr
    
    # Reserve a room, the response will be either the room is reserved or not reserved.
    '''
    What if the room situation is currently Occupied, Not Clean or Cleaning Up 
    '''
    def reserve(self,rmObj):
        if rmObj.situation == 'Occupied': #This means it is an InUseRoom class object, which is a derived from parent class Room
            pass
        if rmObj.situation == 'Not Clean':
            pass
        if rmObj.situation == 'Cleaning Up':
            pass
            
        reply = rmObj.assign(self.reqPpl,self.reqStr)
        if reply['RoomStatus'] == 'Not Reserved':
            return "Room Number "+ str(reply['RoomNumber']) + " cannot be reserved because it is " + reply['RoomSituation']
        else:
            return "Great! Room Number "+ str(reply['RoomNumber']) + " is reserved because it is " + reply['RoomSituation']
    
    #Even if a room is shared by guests, the guests should check in at the same time
    def changeRoomSituationToBusy(self,rmObj):
        rightNow = (dt.now().strftime("%Y-%m-%d %H:%M"))
        now = dt.strptime(rightNow, "%Y-%m-%d %H:%M")
        cIn = dt.strptime(self.checkIn, "%Y-%m-%d %H:%M")
        if (now == cIn):
            rmObj.changeSituation("Occupied");
        
    '''
    Simple method to calculate the costPerPerson, just pass in the rmObj, which has been booked or reserved
    and access the room Object's base price for space and storage
    (Base room cost / number of people in the room ) + (base storage costs * number of items stored).
    '''
    def costPerPerson(self,rmObj):
        ans = 0
        ans = (rmObj.roomCost/self.reqPpl) +(rmObj.strCost/self.reqStr)
        return ans
        
    '''
    If a room is Occupied and we want to make it Available, we pass in the InUseRoom Object (derived class),
    because it will have the checkout time and we can calculate when it will be cleaned and Available
    If a room is not in use and is Not Clean, then we pass in the Room class object, 
    and simply return when it will be Available after cleaning. 
    '''
    def changeRoomSituationToAvailable(self,rmObj):
        
        pass
        



#Following can be uncommented and saved, then on command line run 'python reservation.py' to see the objects created

rm = room.Room(9,9,1,0, "Occupied")
cust = customer.Customer(1,'Suzanne', 'Crown')
rese = Reservation(1, rm.id, cust.id, '2017-05-17 08:00', '2017-05-19 12:05', 2, 1);
print("The Reservation object parameters are:")
print("Reservation Id = " + str(rese.id))
print("Room Id = " + str(rese.roomId))
print("Customer Id = " + str(rese.custId))
print("Check In Time = " + str(rese.checkIn))
print("Check Out Time = " + str(rese.checkOut))
print("Requested number of Guests = " + str(rese.reqPpl))
print("Requested number for storage = " + str(rese.reqStr))


