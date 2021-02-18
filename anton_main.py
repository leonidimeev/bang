from classes import *
import random
import datetime
import sys


def bang(arg):
    def info(*args):
        return 'Which player you want to Bang!? >>> ', 'input'

    def play(target):
        try:
            Player.players[int(target)].banged()
        except ValueError:
            for player in Player.players:
                if player.name == target:
                    player.banged()
                    break

    return {'info': info, 'play': play}[arg[0]](arg[1])


def beer(arg):
    def info(*args):
        return ['player_person_name'], 'info'

    def play(target):
        try:
            player = Player.players[int(target[0])]
            if player.health < player.max_health:
                player.health += 1
                print('Now you have', player.health, 'patrons.')
        except ValueError:
            for player in Player.players:
                if player.name == target[0]:
                    if player.health < player.max_health:
                        player.health += 1
                        print('Now you have', player.health, 'patrons.')
                    break

    return {'info': info, 'play': play}[arg[0]](arg[1])


def saloon():
    pass


def gatling():
    pass


def indians():
    pass


def stagecoach():
    pass


def wells_fargo():
    pass


def store():
    pass


def panic():
    pass


def beautiful_girl():
    pass


def duel():
    pass


def mustang():
    pass


def aim():
    pass


def barrel():
    pass


def jail():
    pass


def dynamite():
    pass


def remington():
    pass


def colt_45():
    pass


def volcanic():
    pass


def winchester():
    pass


def carbine():
    pass


def scofield():
    pass


def angel_eyes():
    pass


def problem_jane():
    pass


def crazy_dog():
    pass


def big_serpent():
    pass


def butch_cassidy():
    pass


def lucky_luke():
    pass


def django():
    pass


def jesse_james():
    pass


def keith_carson():
    pass


def baby_billy():
    pass


def elusive_joe():
    pass


def suzy_lafayette():
    pass


def tom_ketchum():
    pass


def tuco():
    pass


def cold_blooded_rosie():
    pass


def man_without_a_name():
    pass


def sheriff():
    pass


def renegade():
    pass


def outlaw():
    pass


def deputy_sheriff():
    pass


def shuffle_cards(n=100):
    global cards
    for _ in range(n):
        i1 = random.choice([number for number in range(len(cards))])
        i2 = random.choice([number for number in range(len(cards)) if number != i1])
        cards[i1], cards[i2] = cards[i2], cards[i1]


def create_card(card, name, func, count):
    for _ in range(count):
        yield card(name, func)


random.seed(datetime.datetime.now())

cards = list(create_card(ActionCard, 'Bang!',          bang,           25)) +\
        list(create_card(ActionCard, 'Miss!',          None,           12)) +\
        list(create_card(ActionCard, 'Beer',           beer,           6))  # +\
'''
        list(create_card(ActionCard, 'Saloon',         saloon,         1)) +\
        list(create_card(ActionCard, 'Gatling',        gatling,        1)) +\
        list(create_card(ActionCard, 'Indians',        indians,        2)) +\
        list(create_card(ActionCard, 'Stagecoach',     stagecoach,     2)) +\
        list(create_card(ActionCard, 'Wells fargo ',   wells_fargo,    1)) +\
        list(create_card(ActionCard, 'Store',          store,          2)) +\
        list(create_card(ActionCard, 'Panic',          panic,          4)) +\
        list(create_card(ActionCard, 'Beautiful girl', beautiful_girl, 4)) +\
        list(create_card(ActionCard, 'Duel',           duel,           3)) +\
        list(create_card(ItemCard,   'Mustang',        mustang,        2)) +\
        list(create_card(ItemCard,   'Aim',            aim,            1)) +\
        list(create_card(ItemCard,   'Barrel',         barrel,         2)) +\
        list(create_card(ItemCard,   'Jail',           jail,           3)) +\
        list(create_card(ItemCard,   'Dynamite',       dynamite,       1)) +\
        list(create_card(GunCard,    'Remington',      remington,      1)) +\
        list(create_card(GunCard,    'Volcanic',       volcanic,       2)) +\
        list(create_card(GunCard,    'Winchester',     winchester,     1)) +\
        list(create_card(GunCard,    'Carbine',        carbine,        1)) +\
        list(create_card(GunCard,    'Scofield',       scofield,       3))
'''

persons = [
    PersonCard('Angel Eyes ', 4, angel_eyes,
               'Requires 2 "Miss!" to cancel your hits. A successfully applied "Barrel" is considered for one card'
               ' "Miss!"'),

    PersonCard('Problem Jane ', 4, problem_jane,
               'Can play "Bang!" instead of cards "Miss!" and vice versa. By applying "Miss!" instead of "Bang!", she'
               ' cannot play a regular "Bang!" on the same turn, unless she has a "Volcanic".'),

    PersonCard('Crazy dog', 4, crazy_dog,
               'In the recruitment phase of his turn, he must show the second drawn card: if it is a heart or a'
               ' tambourine, he draws another card (without showing it).'),

    PersonCard('Big Serpent', 4, big_serpent,
               'Whenever one of the opponents is killed, he takes all the cards from the deceased\'s hand and from him'
               ' from the game to his hand.'),

    PersonCard('Butch Cassidy', 4, butch_cassidy,
               'Whenever he loses a point of health, immediately draws a card from the deck to his hand.'),

    PersonCard('Lucky Luke', 4, lucky_luke,
               'Whenever it makes a check, it reveals the top 2 cards of the deck and chooses one of them. Then both'
               ' cards are discarded.'),

    PersonCard('Django', 3, django,
               'Whenever he loses a point of health due to a card played by an opponent, blindly draws a card from that'
               ' opponent\'s hand (one for each unit lost). If the opponent has no cards in hand, Django draws nothing.'
               ' None of the players are responsible for the damage from "Dynamite".'),

    PersonCard('Jesse James', 4, jesse_james,
               'In the phase of his turn, he can take the first card either from the deck, or blindly from the hand of'
               ' any opponent. Then he draws the second card from the deck.'),

    PersonCard('Keith Carson', 4, keith_carson,
               'In the phase of his turn, he draws 3 cards from the deck, leaves two of them on his hand, and returns'
               ' the third to the top of the deck face down.'),

    PersonCard('Baby Billy', 4, baby_billy,
               'Any number of "Bang!" cards can be played on its turn.'),

    PersonCard('Elusive Joe', 3, elusive_joe,
               'Do not dismount from his mustang: opponents always see it at a distance of 1 more than usual. If he'
               ' also has a "Mustang" card in play, all distances to Joe are increased by 2 in total.'),

    PersonCard('Suzy Lafayette', 4, suzy_lafayette,
               'Draws a card from the deck as soon as it is left without cards in hand.'),

    PersonCard('Tom Ketchum', 4, tom_ketchum,
               'He can discard 2 cards from his hand at any time during the game in order to immediately restore a unit'
               ' of health. Tom has the right to apply this property several times in a row. You cannot get more health'
               ' than it was at the beginning of the game.'),

    PersonCard('Tuco', 4, tuco,
               'In the phase of his turn, he can take the first card either from the deck or from the top of the'
               ' discard. Then he draws the second card from the deck.'),

    PersonCard('Cold Blooded Rosie', 4, cold_blooded_rosie,
               'Uses its own scope: always sees opponents at a distance of 1 less than usual. If she also has a Sight'
               ' card in play, all distances for Rosie are reduced by 2 in total.'),

    PersonCard('Man-without-a-name', 4, man_without_a_name,
               'He walks everywhere with his barrel: he can cancel a hit aimed at him if he draws a worm. If he has a'
               ' "Barrel" card in play, he gets two chances to cancel the hit (and then he can also play "Miss!").'),
]

Player('Player #1')
Player('Player #2')
Player('Player #3')
Player('Player #4')

if Player.number < 4:
    print('Can\'t play: 4 - 7 players needed.')
    sys.exit()

shuffle_cards()
roles = [
    RoleCard('Sheriff', sheriff),
    RoleCard('Renegade', renegade),
    RoleCard('Outlaw', outlaw),
    RoleCard('Outlaw', outlaw)
]
if Player.number >= 5:
    roles.append(RoleCard('Deputy sheriff', deputy_sheriff))
if Player.number >= 6:
    roles.append(RoleCard('Outlaw', outlaw))
if Player.number == 7:
    roles.append(RoleCard('Deputy sheriff', deputy_sheriff))
person_order = []
role_order = []
for i in range(Player.number):
    person_order.append(random.choice([j for j in range(16) if j not in person_order]))
    role_order.append(random.choice([j for j in range(Player.number) if j not in role_order]))
    Player.players[i].set_person(persons[person_order[i]])
    Player.players[i].set_role(roles[role_order[i]])
    Player.native_gun = GunCard('Colt .45 ', colt_45)
    Player.players[i].name = Player.players[i].person.name
    for _ in range(4):
        Player.players[i].cards_on_hand.append(cards.pop(0))
print([player.name for player in Player.players])

run = True
sheriff_is = [player for player in Player.players if player.role.name == 'Sheriff'][0]
sheriff_index = Player.players.index(sheriff_is)
now_moving = sheriff_index - 1

while run:
    now_moving += 1
    if now_moving == Player.number:
        now_moving = 0
    player = Player.players[now_moving]
    if player.health == 0:
        continue
    print(player.name + '\'s move.' +
          (' (' + player.role.name + ')' if True else '') +
          (' (' + player.person.name + ')') +
          (' ' + str(player.health) + ' patrons.'))
    if player.has_dynamite:
        check_card = cards.pop(0)
    if player.in_jail:
        check_card = cards.pop(0)
    take_cards = [cards.pop(0) for _ in range(2)]
    Player.players[now_moving].move(take_cards)
    print()
