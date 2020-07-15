from random import shuffle

#Creating cards
SUITE = 'H D S C'.split()
#RANKS = '2 3 4 5 6 7'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#mycards =[(s,r) for s in SUITE for r in RANKS]
#print(mycards)
"""
mycards =[(s,r) for s in SUITE for r in RANKS]
print(mycards)
or
mycards=[]
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))

"""


class Deck:
    #Thuis will crteate deck of cards to play
    def __init__ (self):
        print("creating a new ordered deck...Created!")
        self.allcards = mycards =[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    each player has a hand and can remove or add cards to the
    hand.
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()
"""
this player class takes in a name and an instance of hand class object
"""
class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards =[]
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop()) # ore self.hand.remove_card()
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0




#####gameplay###

print("Welcome to War, let's begin...")

#create new deck and split in split_in_half
d = Deck()
d.shuffle()

half1,half2 = d.split_in_half()

#create bopth players
comp = Player("computer", Hand(half1))

name = input("what is your name?")

user = Player(name, Hand(half2))


total_rounds = 0

war_count = 0

while user.still_has_cards() and comp.still_has_cards( ):
    total_rounds+=1
    print("Time for a nwew round")
    print("here are the current standings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count+=1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(tanle_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over, number of rounds: "+str(total_rounds))
print("a war happened " +str(war_count)+" times")
print("Does the computer still have cards? ")
print(str(comp.still_has_cards()))
print("Does the human player still have cards? ")
print(str(user.still_has_cards()))
