
import random

class Card():
    '''base type to represent a card.

    Attributes:
        name: name of card.
        description: description of card.
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n=====\n{}".format(self.name, self.description)

class Deck():
    '''base type to represent stack of cards/tiles

    Attributes:
        cards(list): ordered stack of cards/tiles
    '''
    def __init__(self, cards):
        self.cards = cards

    def isEmpty(self):
        return self.cards == []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def add_card(self, v):
        self.cards.append(v)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.name
        return "Deck contains" + result
