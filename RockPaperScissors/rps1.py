import random

user_wins = 0
computer_wins = 0

options = ['Rock', 'Paper', 'Scissors']

while True:
  user_input = input('Rock/Paper/Scissors or Q to Quit:  ').capitalize()

  if user_input == 'Q':
    break

  if user_input not in options:
    print('Type something valid')
    continue

  random_number = random.randint(0, 2)
  #rock = 0, paper = 1, scissors = 2

  computer_guess = options[random_number]
  print('Computer picked: ', computer_guess)

  if user_input == 'Rock' and computer_guess == 'Scissors':
    print('You Won!')
    user_wins += 1
  elif user_input == 'Paper' and computer_guess == 'Rock':
    print('You Won!')
    user_wins += 1
  elif user_input == 'Scissors' and computer_guess == 'Scissors':
    print('You Won!')
    user_wins += 1
  else:
    print('You lost!')
    computer_wins += 1

print('You won ',user_wins,' times.')
print('Computer won ',computer_wins,' times.')
print('Good Bye!')
