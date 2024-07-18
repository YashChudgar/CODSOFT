import random

def user():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice

def computer():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def Winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ohh!!It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Congratulations!!You won the Game!")
    else:
        print("Oops!!You Lost!")

def Game_Start():
    print("Welcome to Rock, Paper, Scissors Game")
    while True:
        user_choice = user()
        computer_choice = computer()
        Winner(user_choice, computer_choice)
        
        play_again = input("Do you want to play again?\nType yes or no: ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")
Game_Start()
