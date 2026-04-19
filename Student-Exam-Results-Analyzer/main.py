#SCENARIO 3: Student Exam Result Analyzer
#Brief Description
#A school wants to analyse student results for a subject.

#Rules
#•	Program runs for 40 students✔️
#•	Each student enters:
#•	Student number✔️
#•	Test mark (0–100)✔️

#•	Grade classification:
#•	75–100 → Distinction✔️
#•	60–74 → Pass✔️
#•	50–59 → Supplementary✔️
#•	Below 50 → Fail✔️

#Requirements
#•	Display grade per student
#•	Count students in each grade category✔️
#•	Calculate average mark✔️
# •	Use loops and conditional logic

class StudentExam:
    def __init__(self):
        self.student_number = None
        self.test_mark = None
        self.total_student = 5
        self.distinction = 0
        self.passed = 0
        self.supplementary = 0
        self.fail = 0
        self.average_mark = 0
        self.average_mark_final = 0

    def calcs(self):
        self.average_mark += self.test_mark
        self.total_student -= 1

    def results_check(self):
        self.test_mark: int = int(input("Test mark (0–100): "))
        self.average_mark += self.test_mark
        if 75 <= self.test_mark <= 100:
            self.distinction += 1
            self.total_student -= 1
            print("Distinction\n")
        elif 60 <= self.test_mark <= 74:
            self.passed += 1
            self.total_student -= 1
            print("Pass\n")
        elif 50 <= self.test_mark <= 59:
            self.supplementary += 1
            self.total_student -= 1
            print("Supplementary\n")
        elif 0 < self.test_mark < 50:
            self.fail += 1
            self.total_student -= 1
            print("Failed\n")
        elif self.test_mark > 100:
            print("Test mark can't be > 0!\n")
        elif self.test_mark < 0:
            print("Test mark can't be < 0!\n")
        return 0

    def summary(self):
        print("\n--- SYSTEM SUMMARY ---")
        print(f"Distinction: {self.distinction}")
        print(f"Pass: {self.passed}")
        print(f"Supplementary: {self.supplementary}")
        print(f"Fail: {self.fail}")
        self.average_mark_final = (self.average_mark / 500) * 100
        print(f"Average mark: {self.average_mark_final}%")

def main():
    system = StudentExam()

    while system.total_student > 0:
        try:
            student_number = int(input("Student number: "))
            system.results_check()

        except ValueError:
            print("Invalid input!\n")

    system.summary()

if __name__ == "__main__":
    main()




