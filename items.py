
class Item():
    '''base type to represent all items.

    Attributes:
        name: name of item.
        description: description of item.
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n=====\n{}".format(self.name, self.description)


class Omen(Item):
    '''Items required to open the exit. Also summons enemies.

    Attributes:
        name: name of item.
        description: description of item.
    '''
    def __init__(self, name, description):
        super().__init__(name, description)
        

class Weapon(Item):
    '''Items that can damage enemies.

    Attributes:
        name: name of key item.
        description: description of key item.
        damage: amount of hp to reduce.
    '''
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class Armor(Item):
    '''Items that can reduce damage.

    Attributes:
        name: name of key item.
        description: description of key item.
        protection: amount of damage to reduce
    '''
    def __init__(self, name, description, protection):
        self.protection = protection
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nProtection: {}".format(self.name, self.description, self.protection)


class Recovery(Item):
    '''Items that can recover hp.

    Attributes:
        name: name of key item.
        description: description of key item.
        potency: amount of hp to recover.
    '''
    def __init__(self, name, description, potency):
        self.potency = potency
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nPotency: {}".format(self.name, self.description, self.potency)
