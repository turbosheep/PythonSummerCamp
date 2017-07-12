from character import Character

class Player(Character):

	experience = 0
	level = 1

	maxHealth = 100
	currentHealth = 100

	attackValue = 10

	"""docstring for Player"""
	def __init__(self, name="default"):
		super(Player, self).__init__()
		self.name = name

	def levelUp(self):
		if self.experience >= 100:
			self.level = self.level + 1
			self.experience = self.experience - 100
			self.attackValue = self.attackValue + 5
			self.maxHealth = self.maxHealth + 10
			self.currentHealth = self.maxHealth
			return True
		return False

	def gainExp(self, exp):
		self.experience = self.experience + exp
		return levelUp()


		