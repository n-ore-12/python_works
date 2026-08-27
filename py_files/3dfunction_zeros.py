user_input = input("Rock, paper, scissors...")

def rpc_f(user_input):

    if user_input == "rock":
        print("paper")
    elif user_input == "scissors":
        print("rock")
    elif user_input == "paper":
        print("scissors")
    else:
        print("Please try again.")

    print("You lose!!!!")



