import classes
import action_cards
import item_cards

import json
from collections import namedtuple

deck = classes.Deck()
drop = classes.Drop()

roles_path = 'RoleCards.json'
with open(roles_path, 'r') as f:
	data = f.read()
persons = json.loads(data, object_hook = lambda d : namedtuple('X', d.keys())(*d.values()))