#declare my python version and enviroment
#!/usr/bin/env python3
"""
ShopList2.py
This program is a practice my coding
@author Jermain
@version 2017-12-06
"""
#This is my main function call
def shop():
    
    #create a function to show the help menu
    def show_help():
        print("""
    Enter 1 to see help menu
    Enter 2 to see items in list
    Enter 3 to add items to list
    """)
    
    
    #  Loops through all items in the list and prints the current length of list
    def show_item():
        print("There are {} in the list".format(len(items)))
        for item in items:
            print(item)
    
    
    #  function to add items to the list or show, help exit
    def add_item():
        item = (input("Enter item or option: "))
        if item == "1":
            show_help()
        if item == "2":
            show_item()
        if item == "3":
            add_item()
        if item == "4":
            show_item()
            exit()
        items.append(item)
        print("You added a %s to the list." % (item))   #show the item just added to the list
    items = []  #item container
    while len(items) < 10:    # while length of list is less than 10 you can add items
        print("The list has a max of 10 items, you now have {}".format(len(items)))
        try:   # trying to catch errors with user input
            add_item()
        except ValueError:
            print("Enter a string")
    show_item()   # prints the list after program ends
shop() 
            
