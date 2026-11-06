# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

name = "Ahmed"
current_role = "Android Engineer"
learning_goal = "AI engineer"

def calculate_experience(start_year: int, end_year: int) -> int :
    total = end_year - start_year
    return total

def calculate_age(birth_year: int, current_year: int)-> int:
    return current_year - birth_year

def calculate_annual_salary(monthly_salary: float) -> float:
    return monthly_salary * 12

def calculate_remaining_balance(total_monthly_deposit:float, monthly_expense:float) -> float:
    return total_monthly_deposit - monthly_expense

print("Hello, Python!")
print(f"My name is {name}")
print(f"I am {calculate_age(1995, 2026)} years old.")
print(f"I have {calculate_experience(2017, 2026)} years of experience.")
print(f"My current role is {current_role}.")
print(f"My current Annual salary is AED {calculate_annual_salary(100)}.")
print(f"After November salary deposit, and after paying all the bills, remaining amount is AED"
      f" {calculate_remaining_balance(100, 3)} from Salary.")
print(f"My learning goal is {learning_goal}.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
