from datetime import datetime as dt
import room, customer, reservation

class Solution():
    def welcomeMessage(self):
        print("Hello! Welcome to Gilded Rose Inn.")
    
    def createRoomList(self,rmObj,roomList):
        roomList.append(rmObj)
        return roomList
        
    # Find Available Rooms
    def availableRoomsNow(self,roomList):
        total = 0
        print ('---------Room Availability right now--------')
        for each in roomList:
            if each.situation == 'Available':
                total += 1
                print ("Room " + str(each.number) + " with current capacity: "+ str(each.capacity) + " and storage: " + str(each.storage))
        if total == 0:
            print ("Sorry no rooms available right now");
    
    def allRooms(self,roomList):
        print ('---------All Rooms--------')
        for each in roomList:
            print ("Room " + str(each.number) + " with current capacity: "+ str(each.capacity) + " and storage: " + str(each.storage) + " and the room is "+ each.situation+ '.' )
    
sol = Solution()
sol.welcomeMessage()


'''
room1 sleeps 2 people and has 1 storage space
room2 room sleeps 2 people and has 0 storage space
room3 room has 2 storage spaces and sleeps 1 person
room4 room sleeps ONE person and has ZERO storage space
'''
#Creating room objects:
room1 = room.Room(1,1,2,1,"Available")
room2 = room.Room(2,2,2,0, "Cleaning Up")
room3 = room.Room(3,3,1,2, "Not Clean")
room4 = room.Room(4,4,1,0, "Occupied")

# List of room objects
roomList = [];
#call createRoomList() method from Solution class
sol.createRoomList(room1,roomList)
sol.createRoomList(room2,roomList)
sol.createRoomList(room3,roomList)
sol.createRoomList(room4,roomList)

#Print all the rooms with their information
sol.allRooms(roomList)
# Print rooms currently available
sol.availableRoomsNow(roomList)

print ("\n")


# Create a Customer
cust1 = customer.Customer(1,'Suzanne', 'Crown')
# Create a Reservation roomId,custId,checkIn,checkOut,reqPpl,reqStr
res = reservation.Reservation(1, room1.id, cust1.id, '2017-05-17 08:00', '2017-05-19 12:05', 2, 1);
#This means 2 people and 1 storage requested

#Trying to reseve different rooms
print(res.reserve(room1));
print(res.reserve(room2));
print(res.reserve(room3));
print(res.reserve(room4));


print ("Cost per Person for Available room:")
print ("$"+str(res.costPerPerson(room1)));

    
    