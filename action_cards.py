import item_cards

class Action:
	def wait():
		pass
	def shoot(shooter, target, deck, drop):
		if target.with_barrel:
			if item_cards.Barrel().barrel_check(target, deck, drop):
				pass
			else:
				if Miss().miss_detect(target):
					if Miss().will_player_throw_a_miss():

				target.health -= 1
		else:
			if Miss().miss_detect(target):
				print('will ' + target.name + ' throw his miss card?')
				if yes_or_no:
					Miss().miss_throw(target, drop)
				else:
					target.health -= 1
			else: 
				target.health -= 1	
		if (target.health < 1):
			Beer().beer_saving(target)
		else:
			pass
	def yes_or_no():
		answer = input('y/n')
		if answer == 'y':
			return True
		else:
			return False
	def next_player(players, player):
		if player.sit != len(players-1):
			return players[player.sit + 1]
		else:
			return players[0]
	def checking(player, deck, drop, type = 'check'):
		from classes import get_a_card
		checked_card = get_a_card(player, deck, drop, type)
		if checked_card.suit == 'hearth':
			return True
		else
			return False
	
class Bang:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'bang':
				return card
	@staticmethod
	def can_he_shoot(players, shooter, target)
		if shooter.sit > target.sit
			left_sit = target.sit
			dexter_sit = shooter.sit
		else:
			left_sit = shooter.sit
			dexter_sit = target.sit
		right_distance = dexter_sit - left_sit
		left_distance = 0
		for i in range(left_sit):
			left_distance += 1
		for i in range(right_sit, len(players)):
			left_distance += 1
		if left_distance < right_distance:
			distance = left_distance
		else:
			distance = right_distance
		distance -= 1
		distance += target.remoteness
		if distance <= shooter.range:
			return True
		else:
			return False
	@staticmethod
	def bang(players, shooter, target):
		
		if shooter.shooted == False:
			Action().shoot(shooter, target)
			if shooter.equipment[1].name != 'volcanic':
				shooter.shooted = True
			else:
				pass

class Miss:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'miss':
				return card
	@staticmethod
	def miss_detect(player):
		for card in player.cards:
			if card.name == 'miss':
				return True
			else:
				return False
	@classmethod
	def miss_throw(player, drop):
		classes.Drop().player_drop_a_card(player, drop, find(player.cards))

class Dynamite:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'dynamite':
				return card
	def dynamite_put(player):
		player.with_dynamite = True	
		player.equipment.append(find(player.cards))
		player.cards.remove(find(player.cards))
		player.dynamite_just_putted = True	

	def dynamite_check(players, player):
		if player.with_dynamite and not player.dynamite_just_putted:
			if classes.Deck().get_a_card(player, deck, drop, type = 'check'):
				Action().next_player(players, player).with_dynamite == True
				player.with_dynamite == False
			else:

	def dynamite_exposion(player):
		classes.Drop().drop_the_card(drop, player.equipment[0])
		player.health -= 3
		
		if (target.health < 0):
			Player.becomes_dead(target)

class Beer:
	def find(cards):
		for card in cards:
			if card.name == 'beer':
				return card
	def beer_healing(player, card):
		player.health += 1
		classes.Drop().player_drop_a_card(player, drop, card)
	def beer_saving(player):
		if player.health < 1:
			if (Beer().find(target.cards)):
				Beer().beer_healing(target, find(target.cards))
				if (target.health < 1):
					if (Beer().find(target.cards)):
						Beer().beer_healing(target, find(target.cards))
						if (target.health < 1):
							if (Beer().find(target.cards)):
								Beer().beer_healing(target, find(target.cards))
							else:
								Player.becomes_dead(target)
						else:
							Player.becomes_dead(target)
					else:
						Player.becomes_dead(target)
				else:
					Player.becomes_dead(target)
			else:
				Player.becomes_dead(target)
		else:
			pass

class Duel:
	def find(cards):
		for card in cards:
			if card.name == 'duel':
				return card
	def init(duelist_1, duelist_2, drop):
		classes.Drop.player_drop_a_card(duelist_1, drop, find(duelist_1.cards))
		duelists = [duelist_1, duelist_2]
		i = 0
		while True:
			if Bang().find(duelists[i].cards):
				asking_for_bang(duelists[i], drop)
				if i == 0:
					i = 1
				else:
					i = 0
			else:
				loses_in_duel(duelists[i])

	def asking_for_bang(player, drop):
		print('whether the 'str(duelist_1.name) + ' will throw a card?')
		if Action().yes_or_no():
			classes.Drop().player_drop_a_card(player, drop, Bang().find(player.cards))
		else:
			loses_in_duel(player)
	def loses_in_duel(player):
		player.health -= 1
		if (target.health < 1):
			Beer().beer_saving(target)
		else:
			pass

class Shop:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'shop':
				return card
	@classmethod
	def init(players, player, deck, drop):
		classes.Drop.player_drop_a_card(player, drop, find(player.cards))
		count = len(players)
		shop_cards = []
		for i in range(count):
			shop_cards.append(classes.Deck().get_a_card(player, deck, drop, type = 'shop'))
		print('cards in shop: ')
		for card in shop_cards:
			print(card.name)
		current_player = player
		for i in range(count):
			print('which card 'str(current_player) + ' will choose?')
			choise = int(input(' 0 - 6 --> '))
			current_player.cards.append(shop_cards[choise])
			current_player = Action().next_player(players, current_player)

class Indians:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'indians':
				return card
	@classmethod
	def init(players, player, deck, drop):
		classes.Drop.player_drop_a_card(player, drop, find(player.cards))
		for p in players:
			if p!=player:
				print('whether the 'str(p.name) + ' will throw a bang card?')
				if Action().yes_or_no():
					classes.Drop().player_drop_a_card(player, drop, Bang().find(player.cards))
				else:
					loses_to_indians(p)
	def loses_to_indians(player):
		player.health -= 1
		if (target.health < 1):
			Beer().beer_saving(target)
		else:
			pass

class Jail:
	@staticmethod
	def find(cards):
		for card in cards:
			if card.name == 'indians':
				return card
	@classmethod
	def init(shooter, target):
		if (target.role != 'Sheriff'):
			initial_card = find(player.cards)
			classes.Drop.player_drop_a_card(shooter, drop, find(shooter.cards))
			target.in_jail = True
			player.equipment[5] == initial_card
		else:
			print('we cannot put sheriff in jail')
	def jail_check():
		pass
























