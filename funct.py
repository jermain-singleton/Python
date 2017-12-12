#!/usr/bin/env python3

"""

wardrobe.py
This program uses a clothing class to track wardrobe.
@author Jermain Singleton
@version2 2017-12-6
"""

class Clothing(object):
    """
    Clothing class defines a piece of clothing in terms of its name
    or cleanliness.
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
        return "Clothing[name=" + self.name + \
               ",clean=" + str(self.clean) + \
               ",times_worn=" + str(self.times_worn) + \
               ",max_wears=" + str(self.max_wears) + \
                "]"


def main():
    #test clothing class
    myJeans = Clothing("blue jeans", False)
    myShorts = Clothing("shorts")
    myJeans.wear()
    print(myJeans.isClean())
    myJeans.wash()
    print(myJeans.isClean())
    

if __name__ == "__main__":
    main()