#C:/Python/Python36-32

"""
This is for Practice

"""

def help_m():
    print("""
Enter 1 to enter a item
Enter 2 to see help
Enter 3 to see the list
Enter 4 to break the list
""")
def see_l():
    if item in list:
        print(item)
def add_c(list):
    item = input("Enter items you need in list: ")
    list.append(item)
    print("You have entered a", item ," and have", len(list) ,"in the list.")

def main():
    list = []
    while True:
        option = input("Enter a option>  ")
        if option == '4':
            break
        if option == '3':
            see_l()
        if option == '2':
            help_m()
        if option == '1':
            add_c(list)
    print("Goodbye")

if __name__ == "__main__":
    main()