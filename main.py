"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthly_cost = annual_cost / MONTHS_PER_YEAR
    return monthly_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    class_cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return class_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = (annual_cost / SEMESTERS_PER_YEAR) / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    cs1430_cost = credit_cost * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return cs1430_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.

    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits this semester: "))

    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6.   ")
        print("Q. Quit")
        # Show your menu here.

        choice = input("Choose an option: ")

        if(choice == "Q"):
            break
        elif(choice == "1"):
            semester = cost_per_semester(annual_cost)
            print(f"One semester costs ${semester:,.2f}.")
        elif(choice == "2"):
            month = cost_per_month(annual_cost)
            print(f"One month costs ${month:,.2f}.")
        elif(choice == "3"):
            day = cost_per_day(annual_cost)
            print(f"One class day costs ${day:,.2f}.")
        elif(choice == "4"):
            credit = cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${credit:,.2f}.")
        elif(choice == "5"):
            class_cost = cost_per_class(annual_cost, credits)
            print(f"One CS 1430 class meeting costs ${class_cost:,.2f}.")
            


        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
