import classes
import json

roles_path = 'RoleCards.json'
with open(roles_path, 'r') as f:
	data = json.loads(f.read())
	for x in data['Persons']:
		print(x['name'])

