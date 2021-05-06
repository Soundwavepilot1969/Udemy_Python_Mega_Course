#Section 8
# My solution. Maybe too simple? Try using functions which can be called later
listnam = []
while True:
    userinput = input("Say something: ")
    if userinput=='\end':
        break
    else:
        listnam.append(userinput.capitalize())
        continue
    

for items in listnam:
    if items.startswith(('How', 'What','Why', 'Where')):  #Startswith which is a str method accepts tuple values
        print("{}?".format(items))
    else:
        print("{}.".format(items))

# you can do following to get all in one line and add the . or ? not through for loop but through function
print(" ".join(listnam))