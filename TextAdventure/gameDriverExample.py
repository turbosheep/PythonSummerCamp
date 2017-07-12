from character import Character
from player import Player
from enemy import Enemy
from zombie import Zombie


# if you have multiple kinds of enemies, generate them here
def makeEnemy():
	return None

# have the player take their turn, either attack or surrender
def playerTurn(player,enemy):
	notUnderstood = True
	while notUnderstood:
		action = raw_input("Will " + player.name + " attack or surrender? ")

		if action == "attack":
			notUnderstood = False
			print(player.name + " attacks " + enemy.name + "!")
			player.attack(enemy)
		elif action == "surrender":
			notUnderstood = False
			player.currentHealth = 0
			print(player.name + " surrendered")
		else
			print("Command not understood, please try again.")
		
# have the enemy take their turn
def enemyTurn(player,enemy):
	if enemy.currentHealth < 5:
		print(enemy.name + " surrendered!")
		enemy.currentHealth = 0
	else:
		print(enemy.name + " attacks " + player.name + "!")
		enemy.attack(player)

# check if a specific target is dead
def checkDead(target):
	if target.currentHealth <= 0:
		return True
	return False

# print the player and enemy's health
def updateStatus(player,enemy):
	print(player.name + " health: " + str(player.currentHealth))
	print(enemy.name + " health: " + str(enemy.currentHealth))

playAgain = True

print("Hello, welcome to the game!")

#name = input("What is your name?")

while True:
	player = Player()
	enemy = Zombie()

	print(player.name + " encounters " + enemy.name + "!")

	while player.currentHealth > 0: # while player is still alive
		notUnderstood = True
		while notUnderstood:
			
			playerTurn(player,enemy)

			if checkDead(player): # player surrendered
				break
			elif checkDead(enemy): # if enemy dead
				print(player.name + " defeated " + enemy.name + "!")
				enemy = Zombie() # get a new one
				print(player.name + " encounters " + enemy.name + "!")
				continue

			updateStatus(player,enemy)
			enemyTurn(player,enemy)

			if checkDead(enemy): # enemy surrendered
				enemy = Zombie() # get a new one
				print(player.name + " encounters " + enemy.name + "!")
				continue
			elif checkDead(player):
				print(enemy.name + " defeated " + player.name + "!")
				break

			updateStatus(player,enemy)

	restart = input("Would you like to play again? yes/no")

	if restart == "yes":
		continue
	else:
		print("Thanks for playing!")
		break