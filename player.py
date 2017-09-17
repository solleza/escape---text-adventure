
import items, enemies

class Player():
    def __init__(self, x, y):
        self.location_x = x
        self.location_y = y

        self.hp = 100
        self.weapon = "fist"
        self.offense = 10
        self.defense = 0
        self.inventory = {}

        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def get_location(self):
        return self.location_x, self.location_y

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(item, '\n')

    def move(self, x, y):
        self.location_x = x
        self.location_y = y

    def move_north(self):
        self.move(self.location_x, self.location_y-1)

    def move_south(self):
        self.move(self.location_x, self.location_y+1)

    def move_west(self):
        self.move(self.location_x-1, self.location_y)

    def move_east(self):
        self.move(self.location_x+1, self.location_y)

    def grab_item(self, v):
        self.inventory[v.name] = v
        print("You found a {}!".format(v.name))
        print("")
        print(v)

        if isinstance(v, items.Weapon):
            if v.damage > self.offense:
                self.weapon = v.name
                self.offense = v.damage
                print("Your offense is now {}".format(self.offense))

        elif isinstance(v, items.Armor):
            self.defense = v.protection
            print("Your defense is now {}".format(self.defense))

    def heal(self, item):
        self.hp = min(self.hp + item.potency, 100)
        print("You healed! Your HP is now {}".format(self.hp))

    def attack(self, enemy):
        print("You use {} against {}!".format(self.weapon, enemy.name))
        enemy.hp -= self.offense
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{}'s' HP is {}.".format(enemy.name, enemy.hp))

    def take_damage(self, enemy):
        self.hp -= max(enemy.damage - self.defense, 0)
        self.hp = max(self.hp, 0)
        print("Your remaining HP is {}!".format(self.hp))
