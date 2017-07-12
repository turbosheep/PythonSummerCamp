from enemy import Enemy

class Zombie(Enemy):

	attackValue = 1

	maxHealth = 15
	currentHealth = 15

	name = "Zombie"

	"""docstring for Zombie"""
	def __init__(self, level=1):
		super(Zombie, self).__init__(level)