#importing "random" for random operations
import random

# Generate a random number within a range
hidden_number=random.randint(0,100)

#The while loop in the code allows the game to continue running
# until the user correctly guesses the hidden number
#Take notr of the identation as it is defines looping
while True:  

    trial = int(input('Guess a number between 0 to 100:\n'))


    if trial==hidden_number:
        print('Hurray,You Won!!!')
        break  #exits the while loop when the user correctly guesses the hidden number
    elif trial>hidden_number:
    
        print(f'{trial} is too high. Try again')
    else:
        print(f'{trial} is too low. Try again')
  


