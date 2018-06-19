#Given a string of numbers, retrun tru/false if the string is valid if seen from the opposite side
#Eg: "0169", opposite side view is "6910", "234" opposite side view is invalid

#Simple dictionary to store the numbers as indices, and their valid upside down views as values
numberRef = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}   #O(5)

def isValid(input):
    if len(input) == 0:
        return True
    else:
        for each in input:
            if each not in numberRef:
                return False
    return True



print(isValid("131"))
print(isValid("0"))
print(isValid("080169"))
print(isValid(""))

#print (isValid(input("Please enter the number in string format with double quotes")))