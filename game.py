"""
Hi It's my game
"""


class Street:
    """
    Indicates where you are located
    """
    def __init__(self, street):
        self.street = street

    def __str__(self):
        return f'You are on {self.street}'


class Character:
    """
    Describes the character
    """
    def __init__(self, character=None):
        self.character = character

    def __str__(self):
        if self.character is not None:
            return f'{self.character} is here'


class Enemy(Character):
    """
    Inherit from Character and describes enemy
    """
    def __init__(self, character):
        super().__init__(character)

    def __str__(self):
        return f'Run, {self.character} is here!'

    def getter(self):
        """
        :return: str
        """
        return 'enemy'


class Friend(Character):
    """
    Inherit from Character and describes friend
    """
    def __init__(self, character):
        super().__init__(character)

    def __str__(self):
        return f'Cool,{self.character} is here!'

    def getter(self):
        """
        :return: str
        """
        return 'friend'


class Item:
    """
    Describes possible items
    """
    def __init__(self, item):
        self.item = item

    def __str__(self):
        return f'{self.item} is here'


class Food(Item):
    """
    Inherit from Item and describes food
    """
    def __init__(self, item):
        super().__init__(item)

    def __str__(self):
        return f'Yummy, {self.item} is here'


class Weapon(Item):
    """
    Inherit from Item and describes weapon
    """
    def __init__(self, item):
        super().__init__(item)

    def __str__(self):
        return f'The weapon {self.item} is here'


class Person(Item, Character):
    """
    Run all person's actions
    """
    def __init__(self, item, character):
        super().__init__(item)
        Character.__init__(self, character)

    def take(self, backpack):
        """
        Put thing in bag
        :param backpack: list
        :return: str
        """
        backpack.append(self.item)
        return f'The {self.item} is in your bag'

    def fight(self, backpack, input_item):
        """
        Fight with enemy
        :param backpack: list
        :param input_item: str
        :return: str
        """
        for item in backpack:
            if item == input_item:
                del backpack[backpack.index(item)]
                return f'You killed {self.character}'
        else:
            return f'Opps, {self.character} hurt you'

    def threat(self, backpack, input_item):
        """
        Threat friends
        :param backpack: list
        :param input_item: str
        :return: str
        """
        for item in backpack:
            if item == input_item:
                del backpack[backpack.index(item)]
                return f'You threat {self.character}.'
        else:
            return f'You can not threat {self.character}'
