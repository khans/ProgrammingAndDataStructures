#This is currently not being used, however this is the class to create a Gnome Object.
#The Gnome has an id, a squad Id it is associated  with, first and last name.
class Gnome():
    def __init__(self, id, fName, lName, squadId):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.squadId = squadId
        
    
#Following can be uncommented and saved, then on command line run 'python gnome.py' to see the objects created

g = Gnome(1,"Mickey","Guy",1);
print("The Gnome object's parameters are:")
print("Gnome Id = " + str(g.id))
print("Gnome's first name = " + g.fName)
print("Gnome's last name = " + g.lName)
print("Gnome's Squad id = " + str(g.squadId))

    


