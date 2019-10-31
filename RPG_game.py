# make a game where you fight people and you have stats
# Agility 1 = 10% dodge chance
# Make game attack monster
# TODO: Rethink attack mechanic, Rethink & test for average dodge stats also?
# TODO: Add in another move - block
import random


class Monster:
    def __init__(self):
        self.agility = random.randrange(0, 2)  # Increased chance to dodge 0%  - 30%
        self.attack = random.randrange(3, 6)
        self.health = random.randrange(8, 11)

    def attack(self):
        self.attack = random.randrange(3, 6)
        return random.randrange(3, 6)


class Player:
    def __init__(self, role):
        self.role = role
        if self.role == "knight":
            self.agility = 1  # Increase chance to dodge + 10%
            self.attack = 5
            self.health = 10
        elif self.role == "rogue":
            self.agility = 3  # Increase chance to dodge + 30%
            self.attack = 3
            self.health = 6


def main():
    monster = Monster()
    while True:
        job = input("A: Knight\n\rB: Rogue\n\r")

        if job.upper() == "A":
            player = Player("knight")
            break
        elif job.upper() == "B":
            player = Player("rogue")
            break
        else:
            print("Please pick A or B")
    while True:
        player.block = False
        if monster.health > 0 and player.health > 0:
            print("Monster Health:", monster.health)
            print("Player Health:", player.health)
            print()
            move = input("A: Attack\n\rB: Block\n\r")
            print()
            # Player Move
            player.block = False
            if move.upper() == "A":
                monster_dodge = random.randrange(0, 11) + monster.agility
                if monster_dodge <= 10:
                    print("You attacked the monster with", player.attack, "damage!")
                    monster.health -= player.attack
                else:
                    print("The monster dodged your attack!")
            elif move.upper() == "B":
                player.block = True
            # Monster Move
            monster.block = False
            player_dodge = random.randrange(0, 11) + player.agility
            if random.randrange(0, 2) == 0:
                if player.block is False:
                    if player_dodge <= 10:
                        print("The monster attacks you with", monster.attack, "damage!")
                        player.health -= Monster.attack(monster)
                    else:
                        print("You dodged the monsters attack!")
                else:
                    print("You blocked the monsters attack!")
            else:
                monster.block = True

        elif monster.health < 1:
            print("You killed the monster!")
            break
        elif player.health < 1:
            print("The monster killed you!")
            break


if __name__ == "__main__":
    main()
