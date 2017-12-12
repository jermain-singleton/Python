##!/usr/bin/env/ python3

"""
This is to identify car make model year.

"""

class Car():

    """
    Class defines a car.

    """
    def init(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def setMake(self, NewMake):
        self.make = NewMake
    def setModel(self, NewModel):
        self.model = NewModel
    def setYear(self, NewYear):
        self.year = NewYear
    def __str__(self):
        return "Car[make=" + self.make + \
                ",model=" + self.model + \
                ",year=" + self.year + \
                "]"
def Car_info():
    make = input("Enter make of car: ")
    model = input("Enter model of car: ")
    year = input("Enter year of the car: ")
    return (make, model, year)
def show_car(car_list):
    for car in car_list:
        print(car)
# def lookup_car(car_list):
#     carm = input("Car Make: ")
#     for car in car_list:
#         if carm in car.getMake():
#             print(car)
#             look = True
#         else:
#             print("no entry")
#             look = False


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

if __name__ == "__main__":
    main()