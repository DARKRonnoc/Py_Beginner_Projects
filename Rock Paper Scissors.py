import random

def main():
    user_input = None
    opp_choice = None

    print("Choose 'Rock', 'Paper', or 'Scissors'.")
    user_input = str(input())



    while True:
        if user_input in ['Quit', 'quit', 'q', 'Q', 'stop', 'Stop']:
            exit()
        if user_input not in ['Rock', 'rock', 'R', 'r', 'Paper', 'P', 'paper', 'p', 'Scissors', 'scissors', 'S', 's']:
            print("Please pick again.")
            user_input = str(input())
            continue
        if user_input in ['Rock', 'rock', 'R', 'r']:
            user_input = "Rock"
            print("You chose 'Rock'.")
        if user_input in ['Paper', 'P', 'paper', 'p']:
            user_input = "Paper"
            print("You chose 'Paper'.")
        if user_input in ['Scissors', 'scissors', 'S', 's']:
            user_input = "Scissors"
            print("You chose 'Scissors'.")
        break


    opp_list = ["Rock", "Paper", "Scissors"]

    opp_choice = random.choice(opp_list)
    print("The computer chooses: " + opp_choice)

    if user_input == opp_choice:
        print("It's a tie! Try again!")
    elif user_input == "Rock":
        if opp_choice == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_input == "Paper":
        if opp_choice == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_input == "Scissors":
        if opp_choice == "Rock":
            print("You lose!")
        else:
            print("You win!")
    
    return main()
main()
