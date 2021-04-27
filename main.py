import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)  ROCK
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)  PAPER
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)   SCISSORS
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
pc = random.choice(choices)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

print("You choose: \n" + choices[player])
print("The computer chooses: " + pc)

if player == 0:
  if pc == choices[1]:
    print("YOU LOSE")
  elif pc == choices[2]:
    print("YOU WIN")
  else:
    print("TIE")

if player == 1:
  if pc == choices[2]:
    print("YOU LOSE")
  elif pc == choices[0]:
    print("YOU WIN")
  else:
    print("TIE")

if player == 2:
  if pc == choices[0]:
    print("YOU LOSE")
  elif pc == choices[1]:
    print("YOU WIN")
  else:
    print("TIE")