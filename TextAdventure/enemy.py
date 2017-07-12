from character import Character

class Enemy(Character):
	"""docstring for Enemy"""
	def __init__(self, level):
		super(Enemy, self).__init__()
		self.level = level
		self.maxHealth = self.maxHealth + (level * 5)
		self.currentHealth = self.maxHealth
		self.attackValue = self.attackValue + (level * 2)
		