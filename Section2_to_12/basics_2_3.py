# Section 2
# Program that calculates number of hours in a week
print(24*7)
# Path to python interpreter and path to file with & in the beginning can be see when you run the Program
# the terminal takes windows commands. you can run --> py -3.9 basics.py to execute this Program
# typing python or py -3.9 in the terminal will open the python interactive shell/on demand python interpreter and you can type in python code directly.
# python interactive shell can be used for running quick checks
# Can split terminal and file windows

#Section 3
# Python uses implicit declarations for data types so you don't have to explicitly define the data type
# Int String and Floating
x = 10
y = '10'
z = 2.3
print(type(x),type(y),type(z))

# List Datatype. List data type can hold different objects including lists
grades = [9,3,9,6, 'hi', 4.5,[5,6,7]]
print(grades)
#Create list using range. Can also specify step in the range function
grades2 = list(range(0,10))
print(grades2)

# dir(list) will show what can be done with the data type. ex len with list or str
# help(str.upper) will show the help file. Q to quit

# Here upper is a method attached to the str object whereas something like print which doesn't need anything is a function
# dir(__builtins__) will give entire list of python built in functions.

grades_sum = sum(grades2)
print('Average grades = '+str(grades_sum/len(grades2)))

#Count number of occurrences in a list
countnum = grades2.count(6)
print(countnum)

#Dictionary data types for key value pairs
student_dict = {'Mary':20,'Ash':19,'Dave':15}
dict_sum = sum(student_dict.values())
print(dict_sum/len(student_dict))
#Dictionaries can be loaded from files

#Tuple data type. Tuples uses (). Tuples are immutable ie. cannot make changes to it. List are mutable ie. can be changed, appended etc.
student_tuple = (1,2,3,4,(4,5,6))
