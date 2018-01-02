#!/usr/bin/env python3

"""

wardrobe.py
This program uses a clothing class to track wardrobe. I made this off a tutorial.
@author Jermain Singleton
@version2 2017-12-6
"""

class Clothing(object):
    """
    Clothing class defines a piece of clothing in terms of its name
    or cleanliness.
    """
    #Constructor
    def __init__(self, name, clean=True, times_worn=0, max_wears=1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears
    #gettors
    def getName(self):
        return self.name

    def isClean(self):
        return self.clean
    #settors
    def wear(self):
        self.times_worn += 1 
        if self.times_worn >= self.max_wears:
            self.clean = False
    
    def wash(self):
        self.clean = True
        self.times_worn = 0

    #Prints in human readable format
    def __str__(self):
        return "Clothing[name=" + self.name + \
               ",clean=" + str(self.clean) + \
               ",times_worn=" + str(self.times_worn) + \
               ",max_wears=" + str(self.max_wears) + \
                "]"

# where the main function is ran
def main():
    #test clothing class
    myJeans = Clothing("blue jeans", False)
    myShorts = Clothing("shorts")
    myJeans.wear()
    print(myJeans.isClean())
    myJeans.wash()
    print(myJeans.isClean())
    
# is this a standalone or a module?
if __name__ == "__main__":
    main()
