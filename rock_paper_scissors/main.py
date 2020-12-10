import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures = [rock, paper, scissors]

players_choice = int(input( "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if players_choice >= 3 or players_choice < 0:
  print("That is an invalid number... YOU LOSE!")
else:
  print(gestures[players_choice])
  computers_choice = random.randint(0, 2)
  print(f"Computer's choice: \n {gestures[computers_choice]}")

  if players_choice == 0 and computers_choice == 2:
      print("You win!")
  elif computers_choice == 0 and players_choice == 2:
      print("You lose")
  elif computers_choice > players_choice:
      print("You lose")
  elif players_choice > computers_choice:
      print("You win!")
  elif players_choice == computers_choice:
      print("It's a draw!")
