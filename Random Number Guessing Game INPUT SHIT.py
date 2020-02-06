import random

def main():
    

    #first taking two inputs to decide the lower and upper values of our range of numbers
    lower_limit_1 = input("Pick a low number: ")
    upper_limit_1 = input("Pick a high number: ")
    lower_limit = None
    upper_limit = None
    
    while lower_limit != int:
        try:
            lower_limit = int(lower_limit_1)
            break
        except ValueError:
            print("Please pick an integer for your lower limit.")
            lower_limit_1 = input()
   
    while upper_limit != int:
        try:
            upper_limit = int(upper_limit_1)
            break
        except ValueError:
            print("Please pick an integer for your upper limit.")
            upper_limit_1 = input()

    #these are loops that check for inputs being numbers from the user to avoid a crash

    while lower_limit_1 >= upper_limit_1:
        print("Please pick a higher integer for the upper limit.")
        upper_limit_1 = input()
        try:
            upper_limit = int(upper_limit_1)
        except ValueError:
            continue
        
  
        

    numbers = list(range(lower_limit, upper_limit + 1))
    #this turns our inputs into a list using the numbers in our range
    #range doesn't include the "stop" number, so we must add 1

    print(numbers)

    Random_Number = numbers[random.randint(0, len(numbers) - 1)]
    #this function selects a random number from our list
    #the upper limit of this list is the length of our list -1 bc of how Python formats indices

    print(Random_Number)


    guess_check = input("Guess a number from " + str(lower_limit) + " to " + str(upper_limit) + ": ")
    
    try:
        guess = int(guess_check)
    except ValueError:
        print("stuck right here")
        guess = None
    if guess == Random_Number:
        print("Congratulations! You won!")
        print(Random_Number)
            
    while guess != Random_Number:
        try:
            guess = int(guess_check)
        except ValueError:
            print("You a dumb bitch")
        else:
            if guess < lower_limit:
                print("Noiawjndoawdn")
            if guess > upper_limit:
                print("UPPER BITCH")
            elif guess < Random_Number and guess >= lower_limit:
                print("Higher this time bub")
            elif guess > Random_Number and guess <= upper_limit:
                print("Try again but lower: ")
        if guess == Random_Number:
            print("Congratulations! You won!")
        guess_check = input()
        
    Game_state = False
main()