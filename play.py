import random
import time
import os

# Initialize the score
player_wins = 0
computer_wins = 0

# Function to display the game menu
def show_menu():
  os.system('clear')  # Clear the screen
  print("Rock Paper Scissors")
  print("-------------------")
  print("1. Play Rock Paper Scissors")
  print("2. Play Coin Toss")
  print("3. Quit")
  print("-------------------")
  print("Player wins: ", player_wins)
  print("Computer wins: ", computer_wins)

# Function to play a round of rock paper scissors
def play_rps():
  os.system('clear') # Clear the screen
  # Display the options
  print("1. Rock")
  print("2. Paper")
  print("3. Scissors")

  # Get the player's choice
  player_choice = int(input("Enter your choice: "))

  # Generate the computer's choice
  computer_choice = random.randint(1, 3)

  # Determine the winner
  if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
    # Player wins
    print("You win!")
    global player_wins
    player_wins += 1
  elif player_choice == computer_choice:
    # Tie
    print("It's a tie!")
  else:
    # Computer wins
    print("You lose!")
    global computer_wins
    computer_wins += 1

# Function to play a round of coin toss
def play_coin_toss():
  os.system('clear') # Clear the screen
  # Display the options
  print("1. Heads")
  print("2. Tails")

  # Get the player's choice
  player_choice = int(input("Enter your choice: "))

  # Generate the computer's choice
  computer_choice = random.randint(1, 2)

  # Determine the winner
  if player_choice == computer_choice:
    # Player wins
    print("You win!")
    global player_wins
    player_wins += 1
  else:
    # Computer wins
    print("You lose!")
    global computer_wins
    computer_wins += 1

# Main program loop
while True:
  show_menu()
  choice = int(input("Enter your choice: "))

  if choice == 1:
    # Play rock paper scissors
    play_rps()
  elif choice == 2:
    # Play coin toss
    play_coin_toss()
  elif choice == 3:
    # Quit the game
    print("Thanks for playing!")
    break
  else:
    print("Invalid choice. Please try again.")
    
  # Wait 2 seconds before returning to the menu
  time.sleep(2)
