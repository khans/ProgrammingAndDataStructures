from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
while (count<3):
    guess = int(raw_input("Enter a guess:"))
    if guess == random_number:
        print 'You win!'
        break
    count += 1

else:
    print "You lose."