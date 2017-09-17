
class Enemy:
    '''base type for all enemies.

    Attributes:
        name: name of enemy.
        hp: health of enemy.
        damage: damage dealt by enemy
        location_x: x-coord
        location_y: y-coord
    '''
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.location_x = None
        self.location_y = None

    def get_location(self):
        return self.location_x, self.location_y

    def set_location(self, x, y):
        self.location_x = x
        self.location_y = y

    def is_alive(self):
        return self.hp > 0


class Guard(Enemy):
    '''Enemy that stays in one room

    Attributes:
        name: name of enemy.
        hp: health of enemy.
        damage: damage dealt by enemy
        location_x: x-coord
        location_y: y-coord
    '''
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)


class Hunter(Enemy):
    '''Enemy that spawns as far away from the player and chases them

    Attributes:
        name: name of enemy.
        hp: health of enemy.
        damage: damage dealt by enemy
        location_x: x-coord
        location_y: y-coord
    '''
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
