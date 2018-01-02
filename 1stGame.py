#C:\Python36-
"""
Class to be used for practice

"""
class Game(object):
    """
    Lets try some math stuff in game
    """
    def __init__(self, name, hit_point=20):
        self.name = name
        self.hit_point = hit_point
    
    def attack(self):
        print("The creature has hit you for -5")
        self.hit_point -= 5
        print("%s now has %d energies left" %(self.name, self.hit_point))

    def __str__(self):
        return "Game[name=" + self.name + \
                ",hit_point=" + str(self.hit_point) + \
                "]"
def main():
    name = (input("What is your name: "))
    player1 = Game(name)
    print(player1)
    run = True
    while run:
        if option == '1':
            print("You are now advancing into the lighted forest")
            print("A beast attacks")

if __name__ == "__main__":
    main()
