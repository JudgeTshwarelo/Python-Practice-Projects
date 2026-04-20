#SCENARIO 2: Small Business Loan Qualification System
#Brief Description

#A financial service evaluates whether a small business qualifies for a loan.

#Rules
#•	User enters:
#•	Business age (years)✔️
#•	Monthly income✔️
#•	Requested loan amount️️✔️

#•	Qualification conditions:
#•	Business age ≥ 1 year✔️
#•	Monthly income ≥ R5,000✔️
#•	Loan ≤ 6 × monthly income✔️
#•	System processes 30 applications✔️

#Requirements
#•	Display approved and rejected applications✔️
#•	Count rejections by reason✔️
#•	Use functions for qualification checks

system_application_number = 5

approved_applications = 0
rejected_applications = 0

rejected_due_to_business_age = 0
rejected_due_to_low_income = 0
rejected_due_to_loan_exceed_requested = 0
rejected_due_to_loan_cancelled = 0

while system_application_number > 0:
    try:

        business_age: int = int(input("Enter your business age(years): "))
        if business_age >= 4:

            monthly_income: int = int(input("Enter your monthly income: R"))
            if monthly_income >= 5000:
                loan_value: float = 6 * monthly_income
                print(f"You qualify for a loan value of: (R{loan_value})")

                requested_loan_amount: float = float(input("Enter requested loan amount: R"))
                if requested_loan_amount < loan_value:
                    print(f"\nYour business has {business_age} years!")
                    print(f"With monthly income of R{monthly_income}")
                    print(f"You qualify for a loan value of R{loan_value}")
                    print(f"But Requested for R{requested_loan_amount}")

                    confirm_loan: str = input("Confirm details (Yes/No): ")
                    if confirm_loan.upper() == "YES":
                        print(f"Loan of R{requested_loan_amount} is approved.\n")
                        approved_applications += 1
                        system_application_number -= 1
                        print(f"Application left: {system_application_number}")
                    elif confirm_loan.upper() == "NO":
                        print("Loan application canceled!\n")
                        rejected_due_to_loan_cancelled += 1
                        rejected_applications += 1
                    else:
                        print("Invalid Input!\n")

                else:
                    print("[Requested value] can't exceed [Loan value]!\n")
                    rejected_applications += 1
                    rejected_due_to_loan_exceed_requested += 1

            else:
                print("You must have a R5000 monthly income!\n")
                rejected_due_to_low_income += 1
                rejected_applications += 1

        else:
            print("Your business must have 4 years to qualify!\n")
            rejected_due_to_business_age += 1
            rejected_applications += 1

    except ValueError:
        print("Invalid input, try again!\n")

print(f"Rejected applications: {rejected_applications}")
print(f"Approved application: {approved_applications}")

print(f"rejected_due_to_business_age: {rejected_due_to_business_age}")
print(f"rejected_due_to_low_income: {rejected_due_to_low_income}")
print(f"rejected_due_to_loan_exceed_requested: {rejected_due_to_loan_exceed_requested}")
