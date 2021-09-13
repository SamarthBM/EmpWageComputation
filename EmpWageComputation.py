"""
* @Author: Samarth BM.
* @Date: 2021-09-13 20:10  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-13 20:10 
* @Title: :To calculate employee daily and monthly wage.
"""

import random

def calculate_emp_wage():
    """
    Description:
        This function is to check whether employee is present or absent.
        Random fuction is used to check the attendace.

    """    

    print("Welcome to employee wage computation")
    attendance = random.randint(0,1)

    if attendance == 0:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__ == "__main__":
    calculate_emp_wage()