from random import randint
import random as r
options = ['r','p','s']
players = ['bot', 'you']
print("------Welcome to Lang's Rock, Paper, Scissors gamebot------")
print('\n')
count = 0
play = True
play_options = ['n', 'y']
tie = 0

record = [[0,0,0],[0,0,0],[0,0,0]]
previous1 = -1
previous2 = -1


#------------------[Classes and fns]-----------------------------


class player:

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
        self.score = 0


def say(player):
	if player.name == 'bot':
		if player.choice == 0:
			print('The Bot chose rock.')
		elif player.choice == 1:
			print('The Bot chose paper.')
		else:
			print('The Bot chose scissors.')
	else:
		if player.choice == 0:
			print('You chose rock.')
		elif player.choice == 1:
			print('You chose paper.')
		elif player.choice == 2:
			print('You chose scissors.')
	return 


def win(bot,human):
	result = [bot.choice, human.choice]

	if result[0] == result[1]:
		print("It is a tie.")
		return 0

	elif ((int(result[0])- int(result[1]))%3 == 1):
		print("The Bot won.")
		return [1, bot]
	else: 
		print("You won.")
		return [1, human]


def optimal(previous1):
	list = [0,1,2]
	marker = -1
	if (max(record[previous1]) == 0 or record[previous1].count(max(record[previous1])) == 3):
		return randint(0,2)
	elif record[previous1].count(max(record[previous1])) == 2:
		for i in list: 
			if record[previous1][i] is not max(record[previous1]):
				marker = i
			list.pop(marker)
		use = r.choices(list)
		return use[0]
	else:
		for i in list:
			if record[previous1][i] == max(record[previous1]):
				marker = i
		return ((marker+1)%3)


#---------------------------[Actual Code]----------------------------------
bot = player("bot", None)
human = player(None, None)
human.name = input("Hello, what is your name? ")
print("\n")

while play:
	count += 1
	print("The number of your current game: " + str(count))
	print('\n')
	
	# game session
	bot.choice = optimal(previous1)
	human_choice = input("What would you like to choose for this round? \nPlease type 'r' for rock, 'p' for paper, and 's' for scissors: ")

	while human_choice not in options:
		human_choice = input("Your input is not valid. Please type 'r' for rock, 'p' for paper, and 's' for scissors: ")

	for i in [0,1,2]:
		if options[i] == human_choice:
			human.choice = i

	#bot recording 	
	if count == 1:
		previous1 = human.choice
	else:
		previous2 = previous1
		previous1 = human.choice 
		record[previous2][previous1] += 1

	# round result
	print('\n')
	say(bot)
	say(human)
	round_result = win(bot, human)
	if round_result == 0:
		tie += 1
	else:
		round_result[1].score += round_result[0]
	
	print("\n")
	print("CURRENT SCORE")
	print("Bot: " + str(bot.score))
	print(human.name +": "+str(human.score))
	print("Tie: "+str(tie))
	print('\n')

	play_input = input("Would you like to keep playing? \nPlease type 'n' for no or press any other key to continue: ")

	if play_input == 'n':
		play = False
		print('\n')
	else: 
		print('\n')

print("Thank you for trying out the bot. Fuck You.")


	

