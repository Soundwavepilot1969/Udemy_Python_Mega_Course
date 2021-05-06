#prompting user to enter value
x = input("Enter the value :") #input is string so need to typecast into int for doing math functions
print(x+" is what you entered")

#two ways of string formatting
user_input = input("Enter you name: ")
user_surname = input("Enter surname: ")
message_1 = "Hello %s %s!" %(user_input,user_surname) # %s replaced with user_input and user_surname
message_2 = f"Hello {user_input}!" #directly putting in user_input into the string. This is more readable
message_3 = "this is another way Mr.{}".format(user_input) #Another way of formatting text
print(message_1)
print(message_2)
print(message_3)

# Section 7 For Loops
listval = [9.3,7.5,9.9]
for items in listval:
    print(round(items))

# You can also call functions within loops to execute function over the list items

# looping through dictionaries. Iterate through either the keys or the values
student_grades = {'Ash':100,'Dave':34,'Mary':45}
for grades in student_grades.values():
    print(grades)

for key,value in student_grades.items():
    print("{} has a grade = {}".format(key,value)) #another way of formatting strings.

# While loop. It runs as long as the condition is true
# while 1<2:
    # print(1) keeps printing 1. Use ctrl+C to break out of it

i=0
while i<3:
    print(i)
    i+=1  #Prints 0, 1 and 2

#Use break and continue to get out of while loop or continue. Used with True condition for while to keep it looping forever
while True:
    username=input("enter your name:")
    if username=='pypy':
        break
    else:
        continue  #This will keep running the loop until the user enters pypy