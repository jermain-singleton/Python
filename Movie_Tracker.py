def movie():
    print("""
This is a list of my favorite movies that I can \nremember If. I can remeber them then they are good\nto me. I am not movie watcher really.\n
""")
    #list container
    movie_list = []

    #function to see the movie list
    def show_help():
        print("""
    Enter 1 to leave the list
    Enter 2 to see the list
    Enter 3 to show this help again
    """)
    def see_list():
        for x in movie_list:
            print(x)
    def add_movie():
        run = True
        while len(movie_list) < 6:
            item = input("Add movie:  ")
            if item == '1':
                break
            elif item == '2':
                see_list()
            elif item == '3':
                show_help()
            movie_list.append(item)
        print("You have added", item , "the list has", len(movie_list),"movies")
    add_movie()
    print("*****Goodbye you reach the limit*****")
    print()
    see_list()
movie()
    