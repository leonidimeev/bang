import action_cards

class Volcanic:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'volcanic':
				return card
	@staticmethod
	def init(player):
		initial_card = find(player.cards)
		if player.equipment[1] != None:
			classes.Drop().player_drop_a_card(player, drop, initial_card)
		player.equipment[1] == initial_card
		player.cards.remove(initial_card)

class Mustang:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'mustang':
				return card
	@staticmethod
	def init(player):
		initial_card = find(player.cards)
		if player.equipment[3] != None:
			classes.Drop().player_drop_a_card(player, drop, player.equipment[3])
			player.remoteness -= 1
		player.equipment[3] == initial_card
		player.cards.remove(initial_card)
		player.remoteness += 1

class Aim:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'aim':
				return card
	@staticmethod
	def init(player):
		initial_card = find(player.cards)
		if player.equipment[2] != None:
			classes.Drop().player_drop_a_card(player, drop, player.equipment[2])
			player.range -= 1
		player.equipment[2] == initial_card
		player.cards.remove(initial_card)
		player.range += 1


class Barrel:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'barrel':
				return card
	@staticmethod
	def barrel_init(player):
		player.with_barrel == True
		initial_card = find(player.cards)
		player.equipment[4] == initial_card
		player.cards.remove(initial_card)
	@staticmethod
	def barrel_drop(player):
		player.with_barrel == False
	@staticmethod
	def barrel_check(player, deck, drop, type = 'check'):
		action_cards.Action().checking(player, deck, drop, type = 'check')








		