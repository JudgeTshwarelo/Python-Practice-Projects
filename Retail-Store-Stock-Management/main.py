#SCENARIO 5: Retail Store Stock Management
#Brief Description
#A small retail store tracks stock sales for the day.

#Requirements
#•	Prevent selling more than available stock

class RetailStore:
    def __init__(self, product_type, quantity_sold):
        self.product_type = product_type
        self.quantity_sold = quantity_sold

        # •	System runs until daily stock of 100 units is sold👌
        self.system_run = 5
        self.groceries_income = 0
        self.electronics_income = 0
        self.clothing_income = 0

        self.sales_groceries = 0
        self.sales_electronics = 0
        self.sales_clothing = 0
        # •	Calculate total income👌
        self.total_income = 0

    # •	Prices:
    def groceries(self):
        # •	Groceries: R15 per unit👌
        self.groceries_income = 15 * self.quantity_sold
        # •	Display sales per product👌
        self.sales_groceries += self.groceries_income
        print(f"[Grocery of {self.quantity_sold} sales amount to: R{self.groceries_income}]")

    def electronics(self):
        # •	Electronics: R250 per unit👌
        self.electronics_income = 250 * self.quantity_sold
        # •	Display sales per product👌
        self.sales_electronics += self.electronics_income
        print(f"Electronics of {self.quantity_sold} sales amount to: R{self.electronics_income}")

    def clothing(self):
        # •	Clothing: R120 per unit👌
        self.clothing_income = 120 * self.quantity_sold
        # •	Display sales per product👌
        self.sales_clothing += self.clothing_income
        print(f"Clothes of {self.quantity_sold} sales amount to: R{self.clothing_income}")

    def process_user_input(self):
        if self.product_type == 1:
            self.groceries()
        elif self.product_type == 2:
            self.electronics()
        elif self.product_type == 3:
            self.clothing()
        else:
            print("Invalid Product Type!")

    def system_summary(self):
        # •	Calculate total income👌
        self.total_income += self.sales_groceries
        self.total_income += self.sales_electronics
        self.total_income += self.sales_clothing
        print("\n_-_-_-_-_-_-_SYSTEM SUMMARY_-_-_-_-_-_-_")
        # •	Display sales per product👌
        print(f"Sales Groceries: R{self.sales_groceries}")
        print(f"Sales Electronics: R{self.sales_electronics}")
        print(f"Sales Clothing: R{self.sales_clothing}")
        # •	Calculate total income👌
        print(f"Total Store Income: R{self.total_income}")
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

def main():
    retail_store = RetailStore(
        product_type = None,
        quantity_sold = None)

    while retail_store.system_run > 0:
        try:
            # •	User selects product type:👌
            print("~~~~~~~~~SGF STOCK MANAGEMENT~~~~~~~~~")
            print("1 : Groceries")    # •	1 → Groceries
            print("2 : Electronics")  # •	2 → Electronics
            print("3 : Clothing")     # •	3 → Clothing
            retail_store.product_type = int(input("Select product type(1->3): "))

            # •	User enters quantity sold👌
            retail_store.quantity_sold = int(input("Enter quantity sold: "))

            retail_store.process_user_input()

            retail_store.system_run -= 1

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        except ValueError:
            print("Invalid input!")

    retail_store.system_summary()

if __name__ == "__main__":
    main()

