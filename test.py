import classes
import json
import action_cards

# roles_path = 'RoleCards.json'
# with open(roles_path, 'r') as f:
# 	data = json.loads(f.read())
# 	for x in data['Persons']:
# 		print(x['name'])

deck = classes.Deck()
test_player = classes.Player(classes.PersonCard('Tuko','asddes','asdnote',4,'asdability'),'Sheriff')
classes.Deck().get_a_card(test_player, deck)
print(test_player.cards[0].name)