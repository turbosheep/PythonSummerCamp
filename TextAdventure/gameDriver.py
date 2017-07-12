from character import Character
from player import Player
from enemy import Enemy
from zombie import Zombie


# if you have multiple kinds of enemies, generate them here
def makeEnemy():
	return None

# have the player take their turn, either attack or surrender
def playerTurn(player,enemy):
	return None
		
# have the enemy take their turn
def enemyTurn(player,enemy):
	return None

# check if a specific target is dead
def checkDead(target):
	return None

# print the player and enemy's health
def updateStatus(player,enemy):
	return None

playAgain = True

print("Hello, welcome to the game!")

name = input("What is your name?")

while True:
	player = None
	enemy = None

	print(player.name + " encounters " + enemy.name + "!")

	while player.currentHealth > 0: # while player is still alive

		##############PLAYER TURN############
		playerTurn(player,enemy)

		if checkDead(player): # player surrendered
			break
		elif checkDead(enemy): # if enemy dead
			print(player.name + " defeated " + enemy.name + "!")
			enemy = Zombie() # get a new one
			print(player.name + " encounters " + enemy.name + "!")
			continue

		updateStatus(player,enemy)
		#############END OF PLAYER TURN############

		##############ENEMY TURN###################






		############END OF ENEMY TURN##############

	restart = input("Would you like to play again? yes/no")

	if restart == "yes":
		continue
	else:
		print("Thanks for playing!")
		break