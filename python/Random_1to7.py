# Given a function which produces a random integer in the range 1 to 5, write a function which produces a random integer in the range 1 to 7.

def randomGenerator(input):
    if(len(input)%7==0):
        return 1
    else: 
        return ((len(input)%7) + 1)
        
print (randomGenerator(""))
print (randomGenerator("jkfkfj"))
print (randomGenerator("nannananananannanannananare"))
print (randomGenerator("Python is cool"))