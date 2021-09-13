"""
* @Author: Samarth BM.
* @Date: 2021-09-13 20:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-13 20:22 
* @Title: :To calculate employee daily and monthly wage.
"""

import random

def calculate_emp_wage():
    """
    Description:
        This function is to check whether employee is present or absent.
        After checking the attendance, employee daily wage is calculated.

    """    

    print("Welcome to employee wage computation")
    attendance = random.randint(0,1)
    
    wage_per_hr = 20    # Assuming wage per hour as 20

    if attendance == 0:
        print("Employee is present")
        working_hr = 8
    else:
        print("Employee is absent")
        working_hr = 0

    emp_daily_wage = wage_per_hr * working_hr
    print("Employee daily wage is: ", emp_daily_wage)


if __name__ == "__main__":
    calculate_emp_wage()