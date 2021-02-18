import classes
import action_cards
import item_cards

import json
from collections import namedtuple
from random import randint

deck = classes.Deck()
drop = classes.Drop()

roles_path = 'RoleCards.json'
with open(roles_path, 'r', encoding = 'utf-8') as f:
	data = json.load(f)

Persons = []
for person in data["Persons"]:
	Persons.append(classes.PersonCard(person['id'],person['name'],person['description'],person['note'],person['health']))

players = []
number_of_players = 5

if number_of_players < 4:
    print('Can\'t play: 4 - 7 players needed.')
    sys.exit()

randints = []
if number_of_players == 4:
	roles = ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade']
if number_of_players == 5:
	roles = ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade','Helper']
if number_of_players == 6:
	roles = ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade','Helper','Outlaw']
if number_of_players == 7:
	roles = ['Sheriff', 'Outlaw', 'Outlaw', 'Renegade','Helper','Outlaw','Helper']
for i in range(number_of_players):
	rint = randint(1,42)
	if rint not in randints:
		for person in Persons:
			if int(person.id) == rint:
				new_player = classes.Player(i, person, roles[i]) #i eto sit
				randints.append(rint)
				players.append(new_player)

run = True
sheriff_is = players[0]
sheriff_index = 0
now_moving = sheriff_index - 1

while run:
    now_moving += 1
    if now_moving == number_of_players:
        now_moving = 0
    player = players[now_moving]
    print(str(player.sit) + '\'s move.' +
          (' (' + player.role + ')' if True else '') +
          (' (' + str(player.person.name) + ')') +
          (' ' + str(player.health) + ' patrons.'))
    if player.with_dynamite and player.dynamite_just_putted:
    	player.dynamite_just_putted = False
    	action_cards.Dynamite().dynamite_check(players, player)
        
    if player.in_jail:
        if not action_cards.Jail().jail_check(player, deck, drop):
        	now_moving += 1

    take_cards = []
    classes.Deck().get_a_card(player, deck, drop, type = 'default')
    classes.Deck().get_a_card(player, deck, drop, type = 'default')

    classes.Player.move(players[now_moving])
    print()











