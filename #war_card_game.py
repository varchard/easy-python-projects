#war_card_game
import random

'''the classes and objects set up'''

suits = ('Hearts','Clubs','Diamonds','Spades')
'''Tuple holding suits'''
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
        'Jack','Queen','King','Ace')
'''Tuple holding card rankings'''
rank_as_num = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
                'Seven':7,'Eight':8,'Nine':9,'Ten':10,
                'Jack':11,'Queen':12,'King':13,'Ace':14}
'''Dictionary holding card rankings(str) converted to integer'''

class Card:
    '''Objects of type card have suit(string), rank(str), and value(int)
        Print Card returns string of card name'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_as_num[rank]
    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

class Deck:
    '''An object of type Deck will create a list of 52 Card objects
        Method shuffle puts list in random order
        Method deal_one pops card off of all_cards list'''
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                deck_card = Card(suit,rank)
                self.all_cards.append(deck_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop(0)

class Player:
    '''Object Player has attribute name. Player.cards() holds cards dealt.
        Method play_a_card() returns popped card from top of deck.
        Method take_cards() adds won_cards to cards'''
    def __init__(self,name):
        self.name = name
        self.cards = []
    def play_a_card(self):
        return self.cards.pop(0)
    def take_cards(self,won_cards):
        if type(won_cards) == type([]):
            self.cards.extend(won_cards)
        else:
            self.cards.append(won_cards)
    def __str__(self):
        return f'{self.name} holds {len(self.cards)} cards'

'''the functions that make it go'''

def win_check():
    '''Checks win conditions and if players want to continue,
        prints winners name and sets game_on to false when win condition met'''
    global game_on
    if len(player1.cards) == 0:
        print(f'{player2.name} is the winner!')
        game_on = False
    elif len(player2.cards) == 0:
        print(f'{player1.name} is the winner!')
        game_on = False
    else:
        keep_playing = 'BLAH'
        while keep_playing not in ('YES','Y','NO','N'):
            keep_playing = input('Continue playing? Y/N? ').upper()
        if keep_playing in ('Y','YES'):
            print('\n'*50)
            print('The battle continues')
        else:
            game_on = False

def compare_cards(player1_in_play,player2_in_play):
    '''Accepts the cards in play and returns which player wins and list of cards won'''
    cards_to_win = [player1_in_play,player2_in_play]
    def war():
        '''Each player adds 3 cards to cards_to_win, selects a war card and calls compare_cards with new cards'''
       
        cards_to_win.extend([player1.play_a_card(),player1.play_a_card(),player1.play_a_card(),
                            player2.play_a_card(),player2.play_a_card(),player2.play_a_card()])
        print(f'there are now {len(cards_to_win)} cards in the pot')
        war_card1 = player1.play_a_card() 
        war_card2 = player2.play_a_card()
        '''selects the cards to decide the war^ below puts them with the cards to win'''
        print(f'War: {player1.name} pulls {war_card1}, {player2.name} pulls {war_card2}!')
        cards_to_win.extend([war_card1,war_card2])
        '''if statements resolve the war'''
        if war_card1.value == war_card2.value:
            print('Another war!')
            global game_on
            if len(player1.cards) < 4:
                print(f'{player1.name} is out of cards and cannot complete the war. {player2.name} wins on some BS this coder never heard of!')
                game_on = False
                return cards_to_win, player2.name
            elif len(player2.cards) < 4:
                print(f'{player1.name} is out of cards and cannot complete the war. {player2.name} wins on some BS this coder never heard of!')
                game_on = False
                return cards_to_win, player1.name
            else:
                another_war_return = war()
                return another_war_return
        elif war_card1.value > war_card2.value:
            return cards_to_win, player1.name
        elif war_card1.value < war_card2.value:
            return cards_to_win, player2.name
    '''if statements below decide which player wins the cards to win and returns them'''
    if player1_in_play.value == player2_in_play.value:
        print('Its a war!') 
        global game_on
        if len(player1.cards) < 4:
            print(f'{player1.name} is out of cards and cannot complete the war. {player2.name} wins on some BS this coder never heard of!')
            game_on = False
            return cards_to_win, player2.name
        elif len(player2.cards) < 4:
            print(f'{player1.name} is out of cards and cannot complete the war. {player2.name} wins on some BS this coder never heard of!')
            game_on = False
            return cards_to_win, player1.name
        else:
            war_return = war()
            return war_return
    elif player1_in_play.value > player2_in_play.value:
        return cards_to_win, player1.name
    elif player1_in_play.value < player2_in_play.value:
        return cards_to_win, player2.name

'''game set up'''

print('\n'*50)
name1 = input('Player 1, what is your name?')
name2 = input('Player 2, what is your name?')
player1 = Player(name1)
player2 = Player(name2)

'''shuffle and deal'''

start_deck = Deck()
start_deck.shuffle()
p1_cards = []
p2_cards = []
while start_deck.all_cards:
    p1_cards.append(start_deck.deal_one())
    p2_cards.append(start_deck.deal_one())
# p1_cards = [Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace')]
# p2_cards = [Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace'),Card('Spades','Ace')]
print('\n'*50)
player1.take_cards(p1_cards)
player2.take_cards(p2_cards)

'''play'''

game_on = True
while game_on == True:
    player1_in_play = player1.play_a_card()
    player2_in_play =  player2.play_a_card()
    print(f'{player1.name} plays {player1_in_play}, {player2.name} plays {player2_in_play}')
    spoils_to_the_victor = compare_cards(player1_in_play,player2_in_play)
    if spoils_to_the_victor[1] == player1.name:
        player1.take_cards(spoils_to_the_victor[0])
    elif spoils_to_the_victor[1] == player2.name:
        player2.take_cards(spoils_to_the_victor[0])
    print(f'{spoils_to_the_victor[1]} takes the cards')
    print(player1,' and ', player2)
    if game_on == False:
        break
    win_check()