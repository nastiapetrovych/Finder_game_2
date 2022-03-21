import sys
from game import Street, Item, Character, Friend, Food, Person, Weapon, Enemy
backpack = []


def run():
    print('Hi! This is my game')
    streets_lst = ['Kozelnytska', 'Ivana Franka', 'Shevchenka', 'Halytska', 'Siavo', 'Pid Dubom']
    characters_lst = ['Lover', 'Professor', 'Alcoholic', 'Gangster', 'Cousin', 'Pedophile']
    items_lst = ['ice-cream', 'sword', 'chocolate', 'gun', 'juice', 'rock']
    weapon_lst = ['sword', 'gun', 'rock']
    food_lst = ['ice-cream', 'chocolate', 'juice']
    friends_lst = ['Lover', 'Professor','Cousin']
    enemies_lst = ['Killer', 'Alcoholic', 'Pedophile', 'Gangster']
    for element in range(len(streets_lst)):
        p1 = Street(streets_lst[element])
        print(p1)
        if characters_lst[element] in friends_lst:
            p2 = Friend(characters_lst[element])
        elif characters_lst[element] in enemies_lst:
            p2 = Enemy(characters_lst[element])
        print(p2)
        friend_indicator = p2.getter()
        if items_lst[element] in weapon_lst:
            p3 = Weapon(items_lst[element])
        else:
            p3 = Food(items_lst[element])
        print(p3)
        if friend_indicator == 'friend':
            print('________________________________________________')
            p4 = Person(items_lst[element], characters_lst[element])
            input_txt = input('What do you want to do?\nAvailable commands = [take, fight, threat]\n')
            if input_txt == 'take':
                print(p4.take(backpack))
            elif input_txt == 'fight':
                print('You can not fight with  your friend')
            else:
                print('With what do you want to threat a person?')
                print(f'The available items in your bag {backpack}')
                input_3 = input('Enter a name of product here\n')
                if input_3 in food_lst:
                    print(p4.threat(backpack, input_3))
                else:
                    print("OMG, don't hurt your friend")
        else:
            print('________________________________________________')
            p4 = Person(items_lst[element], characters_lst[element])
            input_txt = input('What do you want to do?\nAvailable commands = [take, fight, threat]\n')
            if input_txt == 'fight':
                print('With what do you want to fight?\n')
                print(f'The available items in your bag {backpack}')
                input_2 = input('Enter name of object?\n')
                if input_2 in weapon_lst:
                    txt_new = p4.fight(backpack, input_2)
                    print(txt_new)
                    if txt_new[0] == 'O':
                        sys.exit()
                else:
                    print(f'Opps, {characters_lst[element]} hurts you')
                    sys.exit()
            elif input_txt == 'take':
                print(p4.take(backpack))
                print(f'Opps, {characters_lst[element]} hurts you')
                sys.exit()
            else:
                print('You can not threat your enemy')
    print(f"Great job! You finally reached your destination {streets_lst[-1]}")
    sys.exit()


if __name__ == "__main__":
    run()
