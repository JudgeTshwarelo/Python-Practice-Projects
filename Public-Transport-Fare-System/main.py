#SCENARIO 1: Public Transport Fare System
#Brief Description

#A city bus service charges passengers based on age group and travel distance.
#Rules

#User selects passenger type:
#1 → Student
#2 → Adult
#3 → Senior Citizen

#User enters distance travelled (in km)
#Base fare:
#Students: R2 per km
#Adults: R4 per km
#Seniors: R1.50 per km
#Minimum fare is R10

#The program runs until 50 passengers are processed

#Requirements
#Display total passengers per category
#Display total revenue collected
#Use loops, selection statements, variables, and functions

class Variable:
    seats_avail = 5
    student_passengers = 0
    adult_passengers = 0
    senior_passengers = 0
    total_revenue = 0
    student_price = 2
    adult_price = 4
    senior_price = 1.50
    fare_wage = 0
    minimum_fare = 10

    def __init__(self):
        self.user_input =  None
        self.distance_travelled = None
        self.transport_fare = None

    def get_user_input(self):
        self.distance_travelled: int = int(input("Enter the distance(km) to your destination: "))

    @staticmethod
    def short_distance() -> None:
        print("Distance entered doesn't match your criteria!\n")

    def student(self):
        self.transport_fare = Variable.student_price * self.distance_travelled
        if self.transport_fare < Variable.minimum_fare:
            self.short_distance()
        else:
            print("\n^^^^^^^^^^^^^^^^TICKET DETAILS^^^^^^^^^^^^^^^^^^^^^^^")
            print(f"You're a student and transport fare of {self.distance_travelled}km is: R{self.transport_fare}")
            Variable.seats_avail -= 1
            print(f"Now only {Variable.seats_avail} seats remaining!")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            Variable.student_passengers += 1
            self.total_revenue += self.transport_fare

    def adult(self):
        self.transport_fare = Variable.adult_price * self.distance_travelled
        if self.transport_fare < Variable.minimum_fare:
            self.short_distance()
        else:
            print("\n^^^^^^^^^^^^^^^^TICKET DETAILS^^^^^^^^^^^^^^^^^^^^^^^")
            print(f"\nYou're an Adult and transport fare of {self.distance_travelled}km is: R{self.transport_fare}")
            Variable.seats_avail -= 1
            print(f"Now only {Variable.seats_avail} seats remaining!\n")

            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            Variable.adult_passengers += 1
            self.total_revenue += self.transport_fare

    def senior(self):
        self.transport_fare = Variable.senior_price * self.distance_travelled
        if self.transport_fare < Variable.minimum_fare:
            self.short_distance()
        else:
            print("\n^^^^^^^^^^^^^^^^TICKET DETAILS^^^^^^^^^^^^^^^^^^^^^^^")
            print(f"\nYou're a Senior and transport fare of {self.distance_travelled}km is: R{self.transport_fare}")
            Variable.seats_avail -= 1
            print(f"Now only {Variable.seats_avail} seats remaining!\n")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            Variable.senior_passengers += 1
            self.total_revenue += self.transport_fare

    def bus_projections(self):
        print("\n~~~~~~~~~~~~~~~~FINAL BUS DETAILS~~~~~~~~~~~~~~~~~~~")
        print(f"Total student: {self.student_passengers}")
        print(f"Total adults: {self.adult_passengers}")
        print(f"Total seniors: {self.senior_passengers}")
        print(f"Total revenue: {self.total_revenue}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def main():
    variable = Variable()
    print("********SENOAMADI TRANSPORT SERVICES ********\n")

    while Variable.seats_avail > 0:
        print("-------------------SELECT--------------------")
        print("1 → Student\n"
              "2 → Adult\n"
              "3 → Senior Citizen")
        print("---------------------------------------------")

        user_input: str = input("Select your passenger type(1 - 3): ")

        if user_input == "1":
            variable.get_user_input()
            variable.student()
        elif user_input == "2":
            variable.get_user_input()
            variable.adult()
        elif user_input == "3":
            variable.get_user_input()
            variable.senior()
        else:
            print("Invalid input!")
    else:
        print("The Bus is full sorry!")

    variable.bus_projections()

if __name__ == "__main__":
    main()