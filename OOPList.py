# set class object
class Input(object):
    # constructors
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    #gettors
    def getFirst(self):
        return self.first_name
    def getLast(self):
        return self.last_name
    #settors
    def setFirst(self, NewFirst):
        self.first_name = NewFirst
    def setLast(self, NewLast):
        self.last_name = NewLast
    #human readable print
    def __str__(self):
        return "Input[first_name=" + self.first_name + \
                ",last_name=" + self.last_name + \
                "]"
    #method
    def email_addr(self):
        return self.first_name + self.last_name + "@gmail.com"
#method get and return input from class
def enter_name():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return Input(first_name, last_name)
#method see list with list as parameter
def see_list(list):
    for user in list:
        print(user)
 # calls main function  ask user input and add items to list       
def main():
    user1 = Input("Germain", "Lee")
    run = True
    list = []
    while run:
        print("""
Enter 1 to add to the list
Enter 3 to see the list
Enter 5 to exit the list
""")
        option = input("Pick a option:  ")
        if option == '1':
            list.append(enter_name())
        if option == '3':
            see_list(list)
        if option == '5':
            run = False
if __name__ == "__main__":
    main()

