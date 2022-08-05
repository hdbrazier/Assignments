# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    """Print hello_USERNAME"""
    print("hello_" + user_name.upper() + "!")

hello_name('username')
    

# Question 2 
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Print odd numbers from 1-100"""
    odds = []
    numbers = list(range(1, 101))
    for num in numbers:
        if num % 2 ==1:
            odds.append(num)
        
    print(odds)
    return

first_odds()      
        


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Find the max num"""
    print(max(a_list))

a_list = [5 , 3, 27, 94, 105]
max_num_in_list(a_list)


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Find out if a year is leap year"""
    leap = False
    if a_year % 4 != 0:
        leap = False
    elif a_year % 4 == 0:
        if (a_year % 100 == 0) and (a_year % 400 !=0):
            leap = False 
        else:
            leap = True 
    
    return leap

print(is_leap_year(2000))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
    """Check if numbers are consecutive"""
    for idx, num in enumerate(a_list):
        if idx+1 >= len(a_list):
            return True
        elif num != a_list[idx+1] - 1:
            return False
        
    return True

a_list = [10, 11, 6, 13, 14, 15]
#         0   1   2   3   4   5
print(is_consecutive(a_list))


