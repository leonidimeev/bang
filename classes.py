
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

class RoleCard:
    def __init__(self, role):
        self.role = role

def Sheriff():
	pass


class Player:
    def __init__(self, sit, person, role):
        self.sit = sit
        self.person = person
        self.role = role
        self.health = person.get_health()
        self.range = 1
        self.shooted = False
        if (self.role == 'Sheriff'):
            self.health += 1
        self.remoteness = 0
        self.ability = person.get_ability()
        self.in_jail = False
        self.with_dynamite = False
        self.dynamite_just_putted = False
        self.with_barrel = False
        self.with_mustang = False
        self.with_aim = False
        self.cards = []
        # 0 - dynamite 1 - weapon 2 - aim 3 - mustang 4 - barrel 5 - jail
        self.equipment = [None, None, None, None, None, None]

    def becomes_dead(self):
        pass

class Card:
    def __init__(self, id, name, suit, weight):
        self.id = id
        self.name = name
        self.suit = suit
        self.weight = weight

class Deck:
    @classmethod
    def __init__(self, count = 80):
        self.count = count
        deck = Deck.deck_building()
        self.card = Deck.deck_building()

    @staticmethod
    def deck_building():
        import action_cards, item_cards
        names = ['bang','indians','bang','bang','panic','aim','carbine','miss','remington','bang','bang','indians','scofield','barrel','cutie','miss','barrel','bang','panic','miss','duel','shop','scofield','bang','scofield','cutie','miss','panic','beer','bang','jail','duel','cutie','jail','beer','bang','volcanic','volcanic','gatling','miss','beer','bang','shop','diligence','bang','mustang','cutie','diligence','beer','bang','panic','mustang','bang','winchester','miss','duel','beer','bang','miss','bang','beer','bang','miss','bang','saloon','bang','miss','bang','bang','jail','miss','bang','bang','wales fargo','bang','miss','miss','bang','dynamite','bang']
        suits = ['hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades','hearts','diamonds','clubs','spades']
        weights = ['jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace','jack','queen','king','ace','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','8','9','10','jack','queen','king','ace','8','9','10','jack','queen','king','ace','8','9','10','jack','queen','king','ace','8','9','10','jack','queen','king','ace']
        from random import shuffle
        shuffle(names)
        shuffle(suits)
        shuffle(weights)
        deck = []
        for i in range(80):
            deck.append(Card(i,names[i],suits[i],weights[i]))
        return deck

    @staticmethod
    def get_a_card(player, deck, drop, type):
        from random import randint
        randint = randint(0,deck.count - 1)
        if type == 'check':
            if deck.card[randint].suit == 'hearth':
                return True
            else:
                return False
            Drop().drop_the_card(drop, deck.card[randint])
        elif type == 'default':
            player.cards.append(deck.card[randint])
        elif type == 'shop':
            return deck.card[randint]
        del deck.card[randint]

class Drop:
    @classmethod
    def __init__(self, count = 0):
        self.count = count
        self.card = []

    @staticmethod
    def drop_the_card(drop, card):
        drop.card.append(card)
        drop.count += 1

    @classmethod
    def player_drop_a_card(player, drop, card):
        player.cards.remove(card)
        drop_the_card(drop, card)















