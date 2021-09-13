"""
* @Author: Samarth BM.
* @Date: 2021-09-13 20:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-13 23:16 
* @Title: :To calculate employee daily and monthly wage.
"""

import random

# Constants.
MAX_WORKING_DAYS = 20
MAX_WORKING_HRS = 100

def calculate_emp_wage():
    """
    Description:
        This function is to check whether employee is present or absent.
        Based on the attendance, employee's daily and monthly wage is calculated.
        Total wage is calculated till 20 working days is reached,
        or total 100 working hour is reached.

    """    

    print("Welcome to employee wage computation\n")
    
    wage_per_hr = 20    # Assuming wage per hour as 20
    total_wage = 0
    total_working_hrs = 0
    total_working_days = 0

    # Looping till maximum working days or maximum working hours is achieved.
    while not(total_working_days == MAX_WORKING_DAYS or total_working_hrs == MAX_WORKING_HRS):
        attendance = random.randint(0,2)
        if attendance == fullPresent:
            print("Employee is present for full time")
            working_hr = switcher.get(attendance)
        elif attendance == part_present:
            print("Employee is present for part time")
            working_hr = switcher.get(attendance)
        else:
            print("Employee is absent")
            working_hr = switcher.get(attendance)

        emp_daily_wage = wage_per_hr * working_hr
        print("Employee daily wage is: ", emp_daily_wage)

        total_working_hrs += working_hr
        total_working_days += 1

        total_wage += wage_per_hr * working_hr
    print("Employee monthly wage is: ", total_wage)
    print("Working hrs is: ", total_working_hrs)
    print("Working days is: ", total_working_days)


fullPresent = 0
part_present = 1
absent = 2

switcher = {
    0: 8,
    1: 4,
    2: 0,
}

if __name__ == "__main__":
    calculate_emp_wage()