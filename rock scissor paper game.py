import random
choices = ['rock', 'paper', 'scissor']
computer = random.choice(choices)
player = None
while player not in choices:
    player = input('Enter your choice: ').lower()
if computer == player:
    print('You Won!')
else:
    print('You loose!')
print('Computer', computer)
print('Player', player)

play_again = input('Do you want to play again?')


