
import rooms
import items
import enemies
from player import Player

import board

from cards import Deck
from adjacencygraph import *
import bfs

def unlock_door(omen):
    '''
    '''
    print("Enter three omens: ")
    answer1 = input()
    answer2 = input()
    answer3 = input()
    if answer1 not in omen:
        return False
    if answer2 not in omen:
        return False
    if answer3 not in omen:
        return False
    return True

def encounter(enemy, player):
    return enemy.get_location() == player.get_location()

def settle_encounter(enemy, player):
    while enemy.is_alive() and player.is_alive():
        command = input("Actions: attack, use <item>, open inventory: ")
        if command == "attack":
            player.attack(enemy)

        elif command == "open inventory":
            player.print_inventory()
            continue

        else:
            command = command.split(' ', 1)
            if command[0] == "use":
                item = command[1]
                if item in player.inventory:
                    item = player.inventory[item]
                    if isinstance(item, items.Recovery):
                        player.heal(item)

                    else:
                        print("Item cannot be used this way.")

                else:
                    print("Please Enter a valid item. ")
                    continue

            else:
                print("Please Enter a valid command: ")
                continue
        player.take_damage(enemy)

def room_exists(coord_room, x, y):
    '''
    '''
    return (x, y) in coord_room

def prompt(room_deck, coord_room, player, room):
    '''
    '''
    def get_directions(room_deck, coord_room, player):
        x, y = player.get_location()
        directions = []
        actions = [ "look", "open inventory", "use <item>" ]
        if not room_deck.isEmpty():
            directions = [ "north", "south", "east", "west" ]

        else:
            if room_exists(coord_room, x, y-1):
                directions.append("north")

            if room_exists(coord_room, x, y+1):
                directions.append("south")

            if room_exists(coord_room, x-1, y):
                directions.append("west")

            if room_exists(coord_room, x+1, y):
                directions.append("east")

        for v in directions:
            actions.append( "move {}".format(v) )
        print("Possible actions: ")
        for v in actions:
            print( "\t{}".format(v) )
        return directions

    while True:
        directions = get_directions(room_deck, coord_room, player)
        command = input()

        if command == "look":
            room.intro_text()

        elif command == "open inventory":
            player.print_inventory()

        else:
            command = command.split(' ', 1)
            if command[0] == "use":
                item = command[1]
                if item in player.inventory:
                    item = player.inventory[item]
                    if isinstance(item, items.Recovery):
                        player.heal(item)

                    else:
                        print("Item cannot be used this way.")

                else:
                    print("Please Enter a valid item. ")

            elif command[0] == "move":
                if command[1] not in directions:
                    print("Please Enter a valid direction.")

                elif command[1] == "north": # go north
                    player.move_north()
                    break

                elif command[1] == "south": # go south
                    player.move_south()
                    break

                elif command[1] == "west": # go west
                    player.move_west()
                    break

                elif command[1] == "east": # go east
                    player.move_east()
                    break

            else:
                print("Please enter a valid command.")

def spawn(g, x, y, enemy):
    '''
    '''
    if isinstance(enemy, enemies.Guard):
        enemy.set_location(x, y)

    elif isinstance(enemy, enemies.Hunter):
        v = (x,y)
        new_x, new_y = bfs.get_farthest(g, v)
        enemy.set_location(new_x, new_y)

def update_graph(g, coord_room, x, y):
    '''
    '''
    g.add_vertex( (x,y) )

    if room_exists(coord_room, x-1, y):
        e = ( (x,y), (x-1,y) )
        g.add_edge(e)

    if room_exists(coord_room,  x+1, y):
        e = ( (x,y), (x+1,y) )
        g.add_edge(e)

    if room_exists(coord_room, x, y-1):
        e = ( (x,y), (x,y-1) )
        g.add_edge(e)

    if room_exists(coord_room, x, y+1):
        e = ( (x,y), (x,y+1) )
        g.add_edge(e)

def enemy_movement(g, enemy, player):
    if isinstance(enemy, enemies.Hunter):
        start = enemy.get_location()
        dest = player.get_location()
        x, y = bfs.get_next_v(g, start, dest)
        enemy.set_location(x, y)

def play():
    '''
    '''
    room_deck = board.load_rooms("rooms.txt")
    omen_deck, item_deck = board.load_items("items.txt")
    omen_to_enemy = board.load_enemy("enemies.txt")
    spawned_enemy = []

    start_x, start_y = 0, 0
    g = UndirectedAdjacencyGraph()
    g.add_vertex( (start_x, start_y) )
    coord_room = { (start_x, start_y): rooms.Start() }

    player = Player(start_x, start_y)
    rooms.Start().intro_text()

    while player.is_alive() and not player.victory:
        x, y = player.get_location()
        room = coord_room[(x,y)]
        if room == rooms.Exit():
            player.victory = unlock_door(omen_to_enemy)

        if player.victory:
            rooms.Exit().outro_text()
            break

        if len(spawned_enemy) > 0:
            for enemy in spawned_enemy:
                enemy_movement(g, enemy, player)
                if encounter(enemy, player):
                    settle_encounter(enemy, player)

                if not enemy.is_alive():
                    spawned_enemy.remove(enemy)

                if not player.is_alive():
                    break

        if player.is_alive():
            prompt(room_deck, coord_room, player, room)
            x, y = player.get_location()
            if not room_exists(coord_room, x, y):
                room = room_deck.draw()
                coord_room[(x,y)] = room
                update_graph(g, coord_room, x, y)
                if isinstance(room, rooms.Item_Room):
                    item = item_deck.draw()
                    player.grab_item(item)

                elif isinstance(room, rooms.Omen_Room):
                    omen = omen_deck.draw()
                    player.grab_item(omen)
                    enemy = omen_to_enemy[omen.name]
                    spawn(g, x, y, enemy)
                    spawned_enemy.append(enemy)
            room = coord_room[(x,y)]
            print("Room: {}".format(room.name))

if __name__ == "__main__":
    play()
