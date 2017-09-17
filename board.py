
import csv

import rooms
import items
import enemies

from cards import Deck

def load_rooms(filename):
    '''Takes the csvfile of rooms and returns a shuffled deck of room tiles

    Args:
        filename (csv): name of csv file that contains the list of rooms

    Returns:
        room_deck(Deck): shuffled list of room tiles
    '''
    l = []
    with open(filename) as csvfile:
        contents = csv.reader(csvfile)
        for line in contents:
            if line[0] == "O": # omen room
                name = line[1]
                desc = line[2]
                l.append( rooms.Omen_Room(name, desc) )

            elif line[0] == "I": # item room
                name = line[1]
                desc = line[2]
                l.append( rooms.Item_Room(name, desc) )

            elif line[0] == "E": # NULL - empty room
                name = line[1]
                desc = line[2]
                l.append( rooms.Empty_Room(name, desc) )

    csvfile.close() # close file

    l.append( rooms.Exit() )
    room_deck = Deck(l)
    room_deck.shuffle()
    return room_deck

def load_items(filename):
    '''Takes the csvfile of items and converts it a shuffled deck of items/omens

    Args:
        filename (csv): name of csv file that contains list of item cards

    Returns:
        omen_deck (Deck): shuffled list of all omen cards
        item_deck (Deck): shuffled list of all other items
    '''
    l_omen = []
    l_item = []
    with open(filename) as csvfile:
        contents = csv.reader(csvfile)
        for line in contents:
            if line[0] == "O": # omen
                name = line[1]
                desc = line[2]
                l_omen.append( items.Omen(name, desc) )

            elif line[0] == "W": # weapon
                name = line[1]
                desc = line[2]
                damage = int( line[3] )
                l_item.append( items.Weapon(name, desc, damage) )

            elif line[0] == "A": # armor
                name = line[1]
                desc = line[2]
                protection = int( line[3] )
                l_item.append( items.Armor(name, desc, protection) )

            elif line[0] == "R": # recovery
                name = line[1]
                desc = line[2]
                potency = int( line[3] )
                l_item.append( items.Recovery(name, desc, potency) )

    csvfile.close() # close file

    omen_deck = Deck(l_omen)
    omen_deck.shuffle()
    item_deck = Deck(l_item)
    item_deck.shuffle()
    return omen_deck, item_deck

def load_enemy(filename):
    '''Takes the csvfile of enemies and converts it into a dicts of enemies with
    omens as keys

    Args:
        filename (csv): name of csv file that contains list of rooms

    Returns:
        d(dict): dictionary of enemies. keys are omens.
    '''
    d = dict()
    with open(filename) as csvfile:
        contents = csv.reader(csvfile)
        for line in contents:
            if line[0] == "G":
                omen = line[1]
                name = line[2]
                hp = int( line[3] )
                damage = int( line[4] )
                d[omen] = enemies.Guard(name, hp, damage)

            elif line[0] == "H":
                omen = line[1]
                name = line[2]
                hp = int( line[3] )
                damage = int( line[4] )
                d[omen] = enemies.Hunter(name, hp, damage)

        csvfile.close() # close file
    return d
