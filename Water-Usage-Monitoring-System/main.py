#SCENARIO 4: Water Usage Monitoring System
#Brief Description
#A municipality tracks household water usage to detect overuse.

#Rules
#•	User enters:
#•	Household ID✔️
#•	Monthly water usage (kilolitres)✔️

#•	Billing:
#•	First 10 kL → Free✔️
#•	11–25 kL → R12 per kL✔️
#•	Above 25 kL → R20 per kL✔️
#•	System processes 25 households✔️

#Requirements
#•	Display bill per household✔️
#•	Count households exceeding 25 kL✔️
#•	Calculate total revenue✔️

class MonitoringSystem:
    def __init__(self):
        self.household_id = None
        self.water_usage = None
        self.total_household = 5
        self.water_bill = 0
        self.household_greater_than_25 = 0
        self.total_revenue = 0

    def details(self):
        print(f"Water bill for house ID-[{self.household_id}] is: R{self.water_bill}!\n")
        self.total_revenue += self.water_bill

    def process_bill(self):
        self.household_id = int(input("Enter house ID: "))
        self.water_usage = int(input("Enter water usage(kl): "))
        if 0 < self.water_usage < 10:
            print(f"Water bill for house ID-[{self.household_id}] is: free!\n")
        elif 11 < self.water_usage < 25:
            self.water_bill = 12 * (self.water_usage - 10)
            self.details()
        elif self.water_usage > 25:
            self.water_bill = 20 * (self.water_usage - 10)
            self.household_greater_than_25 += 1
            self.details()
        else:
            print("Invalid water usage input!\n")

    def system_summary(self):
        print("\n---------SYSTEM SUMMARY---------")
        print(f"Households exceeding 25 kL: {self.household_greater_than_25}")
        print(f"Total Revenue: R{self.total_revenue}")
        print("--------------------------------")

def main():
    monitoring_system = MonitoringSystem()

    while monitoring_system.total_household > 0:
        print("-------JUDGE WATER USAGE SYSTEM-------")
        try:

            monitoring_system.process_bill()
            monitoring_system.total_household -= 1

        except ValueError:
            print("Invalid Input!\n")

    monitoring_system.system_summary()

if __name__ == "__main__":
    main()