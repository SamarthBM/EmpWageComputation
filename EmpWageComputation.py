"""
* @Author: Samarth BM.
* @Date: 2021-09-13 20:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-13 23:45 
* @Title: :To calculate employee daily and monthly wage.
"""

import random

# Constants.
MAX_WORKING_DAYS = 20
MAX_WORKING_HRS = 100

def get_working_hrs(attendance):
    """
    Description:
        This function is to get the working hour of employee.

    Args:
        attendance: It might be full time present, part time present and absent.

    Return: Working hours i.e 8, 4 or 0.
    """    

    if attendance == full_Present:
        print("Employee is present for full time")
        working_hr = 8
    elif attendance == part_present:
        print("Employee is present for part time")
        working_hr = 4
    else:
        print("Employee is absent")
        working_hr = 0

    return working_hr



def calculate_emp_wage():
    """
    Description:
        This function is to calculate employee daily and monthly wage.
        Employee monthly wage is calculated for the below condition:
        Until total 20 working days or total 100 working hrs is achieved.

    """    

    print("Welcome to employee wage computation\n")
    
    wage_per_hr = 20    # Assuming wage per hour as 20
    total_wage = 0
    total_working_hrs = 0
    total_working_days = 0

    # Looping till maximum working days or maximum working hours is achieved.
    while not(total_working_days == MAX_WORKING_DAYS or total_working_hrs == MAX_WORKING_HRS):
        attendance = random.randint(0,2)
        emp_attendance = switcher.get(attendance)
        working_hrs = get_working_hrs(emp_attendance)
        emp_daily_wage = wage_per_hr * working_hrs
        print("Employee daily wage is: ", emp_daily_wage)

        total_working_hrs += working_hrs
        total_working_days += 1
        total_wage += wage_per_hr * working_hrs

    print("Employee monthly wage is: ", total_wage)
    print("Working hrs is: ", total_working_hrs)
    print("Working days is: ", total_working_days)


full_Present = 0
part_present = 1
absent = 2

switcher = {
    0: full_Present,
    1: part_present,
    2: absent,
}

if __name__ == "__main__":
    calculate_emp_wage()