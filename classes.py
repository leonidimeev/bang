class ActionCard:
    def __init__(self, name, action):
    	self.name = name
    	self.action = action

def bang():
	pass

class ItemCard:
	def __init__(self, name, ability):
		self.name = name
		self.ability = ability

def Volkanik():
	# Player.number of shots += 100000
	pass

def Vinchester():
	# Player.rangeofshot += 5
	pass 

class PersonCard:
    def __init__(self, name, description, note, health, ability):
        self.name = name
        self.description = description
        self.note = note
        self.health = health
        self.ability = ability
    def get_health(self):
        return self.health
    def get_ability(self):
    	return self.ability

def angel_eye():
	pass
	# player.rangeofshot += 1
def tuko_damaged():
	pass
	# tyanet kartu 
def lucky():
	pass
	# tyanet dve karty pri proverke

class RoleCard:
    def __init__(self, role):
        self.role = role

def Sheriff():
	pass


class Player:
    def __init__(self, person, role):
        self.person = person
        self.role = role
        self.health = person.get_health()
        self.range = 1
        self.shots = 1
        if (self.role == 'Sheriff'):
            self.health += 1
        self.remoteness = 0
        self.ability = person.get_ability()
        self.in_jail = False
        self.with_dynamite = False
        self.with_barrel = False
        self.with_mustang = False
        self.with_aim = False

















