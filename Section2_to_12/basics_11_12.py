# section 11 - processing files
myfile = open(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12\sample.txt') #This only creates a file object and stores it in myfile
# print(myfile.read()) #Reads the file and prints

#if you run the myfile.read() method it will move the cursor from the beginning to the end of the file. 
# On running myfile.read again it will print an empty string. So its better to store myfile.read() into a variable and print that instead
# This should be done right at the first read method, when its executed for the first time

content = myfile.read()
myfile.close() #Closes the file but content will still hold the value
print(content)

# Using with to open files is a better way to do the above
with open(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12\sample.txt') as myfile: #convention is f instead of myfile
    content = myfile.read()
    # Using with file closing is implicitly done
print(content)

# Writing text to a file. Use mode 'w' in open
with open(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12\new_sample.txt','w') as myfile: 
    #convention is f instead of myfile. Created new file new_sample
    myfile.write('Tomato\nOnion\nCarrot') #writes this into the file. Can do multiple writes
mynewfile = open(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12\new_sample.txt')
print(mynewfile.read())

# Adding / writing to a file without overwriting existing content
# Use mode 'a' to append to a file. Use + sign with a to read and write at same time
with open(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12\new_sample.txt','a+') as nf:
    nf.write('\nNew entry')
    nf.seek(0) #moves cursor back to first position. If this not done then contentnew will be empty as cursor at end of line after above write
    contentnew=nf.read()
print(contentnew)

# Section 12 - Modules
# Use dir(__builtins__) to get builtin functions in python. Run this in python shell. For list of methods in a data type --> dir(str)

# For modules import the package ex. --> import time
# sys.builtin_module_names will give list of modules. import sys and then run this to get entire list.
# sys is a module to change the python runtime and you're calling this module to get entire list in above command

# import the module needed - sys, time, array, builtins etc. 
# you can get help as well for explanation of the module and builtin function inside the module help(time.sleep)

#program to read content of a file every 10 seconds. Use the time.sleep to wait 10 seconds inside a while loop to keep reading the file
# import time
# while True:
#     with open('filename.txt') as file:
#         print(file.read())
#         time.sleep(10)

# The builtin modules like sys and time are written in C. 
# There are standard python modules like os which are written in python. Builtin modules contain builtins objects
import os
import sys
print(sys.prefix)
if os.path.exists(r'D:\All_Git_Projects\Udemy_Python_Mega_Course\Section2_to_12'):
    print('Yes')
else:
    print('No')

# Apart from builtin and standard modules there are also third party modules you can import like pandas, tkinter etc.
# A collection of modules is called a package
# Modules/packages are also called libraries