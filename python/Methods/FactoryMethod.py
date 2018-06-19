class Dog:
  def __init__(self,name):
    self.name = name
  
  def speak(self):
    return "Woof"

#Now create a Cat class:
class Cat:
  def __init__(self,name):
    self.name = name
  
  def speak(self):
    return "Meow"

#Factory method
def getPet(pet="dog"):
  pets= dict(dog=Dog('Hope'),cat = Cat('Peace'))
  print(pets)
  return pets[pet]


import time
 
def sleeper():
    while True:
        # Get user input
        num = input('How long to wait: ')
 
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
 
        # Run our time.sleep() command,
        # and show the before and after time
        print('Before: %s' % time.ctime())
        time.sleep(num)
        print('After: %s\n' % time.ctime())
 
 
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()