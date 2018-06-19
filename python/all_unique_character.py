#Function to confirm whether a given string contains all unique characters
def all_unique_char(str):
    asciis = []
    
    # if the length of input string is greater than 256 possible ascii characters, then return false
    if len(str)>256:
        return False
    
    for each in str:
        if ord(each) in asciis:
            return False
        else:
            asciis.append(ord(each))
    return True


print all_unique_char("Hello") #False
print all_unique_char("") #True
print all_unique_char("o") #True
print all_unique_char("I LoveU") #True