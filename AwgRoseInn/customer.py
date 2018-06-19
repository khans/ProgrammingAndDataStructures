'''
Customer has an id, has a first name, 
and has a last name.
'''
class Customer():
    def __init__(self,id,fName,lName):
        self.id = id
        self.fName = fName
        self.lName = lName
        
    
    
#Following can be uncommented and saved, then on command line run 'python customer.py' to see the objects created

c = Customer(1,"Minnie","Rose");
print("The Customer object's parameters are:")
print("Customer Id = " + str(c.id))
print("Customer's first name = " + c.fName)
print("Customer's last name = " + c.lName)


        