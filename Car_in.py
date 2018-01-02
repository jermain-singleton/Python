##!/usr/bin/env/ python3

"""
This is to identify car make model year.
I made this my self to with a simple loop to practice OOP
"""

class Car():

    """
    Class defines a car.

    """
    #constructor
    def init(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    #gettor methods
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    
    #settor methods
    def setMake(self, NewMake):
        self.make = NewMake
        
    def setModel(self, NewModel):
        self.model = NewModel
        
    def setYear(self, NewYear):
        self.year = NewYear
    
    #Prints my code human readable
    def __str__(self):
        return "Car[make=" + self.make + \
                ",model=" + self.model + \
                ",year=" + self.year + \
                "]"
                
#Method to get input from the user                
def Car_info():
    make = input("Enter make of car: ")
    model = input("Enter model of car: ")
    year = input("Enter year of the car: ")
    return (make, model, year)

#Method to show the contents of in the list
tems in the list
def show_car(car_list):
    for car in car_list:
        print(car)

#where the main program is ran with user input options
def main():
    car_list = []
    while True:
        ans = input("Enter Option: ")
        if ans == '1':
            break
        if ans == '2':
            car_list.append(Car_info())
        if ans == '3':
            show_car(car_list)
        # if ans == '4':
        #     lookup_car(car_list)
    show_car(car_list)
    print("Have a good day")

#ask if this is the main program
if __name__ == "__main__":
    main()
