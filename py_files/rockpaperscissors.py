user_input = input("Rock, paper, scissors... ")

def rps_f(user_input):
    if user_input == "paper":
        print("Scissors. You lose!")
    elif user_input == "scissors":
        print("Rock. You lose!")
    elif user_input == "rock":
        print("Paper! You lose!")
    else:
        print("Try again.")

rps_f(user_input)