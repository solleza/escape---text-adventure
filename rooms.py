import textwrap

class Room():
    '''base type to represent all rooms.

    Attributes:
        name: name of room.
        description: description of item.
        x: x-coord
        y: y-coord
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.x = None
        self.y = None

    def set_coord(x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class Omen_Room(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def intro_text(self):
        for line in textwrap.wrap(self.description, 50):
            print(line)

    def modify_player(self, player):
        pass # Room has no action on player


class Item_Room(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def intro_text(self):
        for line in textwrap.wrap(self.description, 50):
            print(line)

    def modify_player(self, player):
        pass # Room has no action on player


class Empty_Room(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def intro_text(self):
        for line in textwrap.wrap(self.description, 50):
            print(line)

    def modify_player(self, player):
        pass # Room has no action on player


class Start(Room):
    def __init__(self):
        self.x = 0
        self.y = 0
        super().__init__("Bedroom", None)

    def intro_text(self):
        print("""
        You find yourself in an old bedroom with no memory of who you are or how
        you got there. You hear inhumane noises coming from outside the door, but
        have no choice but to try and find a way out.
        """)

    def modify_player(self, player):
        pass # Room has no action on player


class Exit(Room):
    def __init__(self):
        super().__init__("Elevator", None)

    def intro_text(self):
        print("""
        In front of you is an elevator with a console attached. A giant neon sign
        with the words "EXIT" on it hangs above. The console asks for three passphrases.
        What could they be?
        """)

    def outro_text(self):
        print("""
        You get into the elevator, and sure enough it starts moving... downward?
        Suddenly, you wake up in your own bed in a cold sweat. Seeing your alarm
        clock, you realize you're late to your CMPUT 275 class! After spending a
        night working on your term project, you rush out of your house and catch
        the bus to school.
        """)

    def modify_player(self, player):
        player.victory = True
