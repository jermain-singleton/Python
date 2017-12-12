#declare my python version and enviroment
#!/usr/bin/env python3
"""
funct.py
This program is a practice my skills
@author Jermain
@version 2017-12-06
"""
def shop():

    def show_help():
        print("""
    Enter 1 to see help menu
    Enter 2 to see items in list
    Enter 3 to add items to list
    """)

    def show_item():
        print("There are {} in the list".format(len(items)))
        for item in items:
            print(item)

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
        print("You added a %s to the list." % (item))
    items = []
    while len(items) < 10:
        print("The list has a max of 10 items, you now have {}".format(len(items)))
        try:
            add_item()
        except ValueError:
            print("Enter a string")
    show_item()
shop() 
            