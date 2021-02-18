
class Action:
	def wait():
		pass
	
class Bang:
	def bang(shooter, target):
		if miss_check(shooter, target):
			pass
		else:
			target.health -= 1
		if (target.health < 0):
			Player.becomes_dead(target)

class Miss:
	def __init__(self,id):
		self.id = id
		self.name = 'miss'
		
	def target_give_miss(action):
		if (action != None):
			result = action
			return(result)
		else:
			return(False)

	def target_checked_barrel(target):
		return(False)

	def miss_check(shooter, target):
		miss = False
		if target_give_miss(target):
			miss = True
		if target_checked_barrel(target):
			miss = True
		return(miss)

	def miss(target):
		target_give_miss(True)

class Dynamite:
	def dynamite_put(target):
		player.with_dynamite = True	
		player.dynamite_just_putted = True	

	def dynamite_check(target):
		if player.with_dynamite and not player.dynamite_just_putted:
			player.dynamite_just_putted = False






















