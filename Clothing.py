"""
RichardWardrobeOOP.py
This program uses a Clothing class to keep track of my wardrobe.
@version 2
"""
class Clothing(object):
    """
    The Clothing class defines a piece of clothing in terms of 
    its name and its cleanliness.
    """
    def __init__(self, name, clean=True, times_worn=0, max_wears=1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean
    
    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean = False
    
    def wash(self):
        self.clean = True
        self.times_worn = 0

    def __str__(self):
        return  "Clothing[name=" + self.name + \
                ",clean=" + str(self.clean) + \
                ",times_worn=" + str(self.times_worn) + \
                ",max_wears=" + str(self.max_wears) + \
                "]"

class Shirt(Clothing):
    def __init__(self, name, clean=True, times_worn=0, max_wears=1, shortsleeves=True):
        super().__init__(name, clean, times_worn, max_wears)
        self.shortsleeves = shortsleeves
    def hasShortSleeves(self):
        return self.shortsleeves
    def __str__(self):
        return "Shirt[" + super().__str__() + \
               "shortsleeves=" + str(self.shortsleeves) + "]"


def main():
#test area
    myClothes = []
    myClothes.append(Clothing("blue jeans", False))
    myClothes.append(Clothing("baseball cap", True, 20, 1000))
    myClothes.append(Clothing("jacket", True, 20, 100))
    myClothes.append(Shirt("t-shirt", True, 0, 1, True))
    myClothes.append(Shirt("dress shirt", True, 0, 1, False))

    print("\n===== Full Wardrobe =====")
    for i in range(len(myClothes)):
        print(myClothes[i])
    print("\n===== Clean clothes =====")
    for i in range(len(myClothes)):
        if myClothes[i].isClean():
            print(myClothes[i])
    print("\n===== Dirty clothes =====")
    for i in range(len(myClothes)):
        if not myClothes[i].isClean():
            print(myClothes[i])
    print("\n===== Shirts ============")
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            print(myClothes[i])

    


if __name__ == "__main__":
    main()