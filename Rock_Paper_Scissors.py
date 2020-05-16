#rock paper scissors

import random 

shapes = ['rock', 'paper', 'scissors']

computer_score = [0]
player_score = [0]

#start game
def start_game():
	answer = ''

	while answer != 'y' or answer != 'n':
		answer = input('Would you like to play rock, paper, scissors? yes or no: ').lower()
		if answer == 'yes':
			print("Let's play!")
			return 'yes'
		elif answer == 'no':
			print('Quitter...')
		else:
			print("It's a yes or no question!")
	
#function to ask for player input and assign input to player
def player_input():
	
	player = ''
	#ask for player shape until it == rock paper or scissors
	while player != 'rock' or player != 'paper' or player != 'scissors':
		player = input('Please choose rock, paper, or scissors: ').lower()
		if player == 'rock' or player == 'paper' or player == 'scissors':
			return player
		else:
			print('Hey! Stop cheating!')
			continue

#function to generate random computer play
def computer_input():
	computer = random.choice(shapes)
	print(f'Computer chose {computer}')
	return computer
	
#function to check round winner
def round_winner(computer, player):
	if (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
		computer_score[0] += 1
		print('Computer won this round!')
		return computer_score 

	elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
		player_score[0] += 1
		print('You won this round!')
		return player_score 
		
	else:
		print('Draw!')

#function to declare a winner
def winner_check(computer_score, player_score):
	if computer_score[0] == 3:
		print('HAHAHAHAHAHA YOU LOSE!!!')
		return computer_score[0]
				
	elif player_score[0] == 3:
		print('YOU ARE THE WINNER!!!')
		return player_score[0]
						
	else:
		print(f'Player: {player_score[0]}\nComputer: {computer_score[0]}\nAnother round!')
		
#function to ask player to play again
def play_again():
	play_again =  input('Would you like to play again? yes or no: ').lower()
	if play_again == 'yes':
		player_input()
	else:
		print('Thanks for playing!')

if __name__ == '__main__':
	
	print('Welcome to rock, paper, scissors!\nPaper beats rock, rock beats scissors and scissors beats paper.\nFirst to 3 wins!')
	if start_game() == 'yes':
		game_on = True
	else:
		game_on = False
	#game play
	while game_on:
		player_shape = player_input()
		computer_shape = computer_input()
		round_winner(computer_shape, player_shape)
		winner_check(computer_score, player_score)
		if computer_score[0] == 3 or player_score[0] == 3:
			game_on = False
			play_again()
		else:
			continue

		