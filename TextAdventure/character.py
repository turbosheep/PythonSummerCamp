class Character(object):

	name = "default"

	maxHealth = 100
	currentHealth = 100

	level = 1

	attackValue = 10

	"""docstring for Character"""
	def __init__(self):
		super(Character, self).__init__()
		

	def attack(self, target):
		target.takeDamage(self.attackValue)

	def takeDamage(self, damage):
		self.currentHealth = self.currentHealth - damage