# Section 4
# Use cls or clear to clear the terminal screen
# Use exit() to get out of python shell

# Use list.append to add items to list
temp=[9.3,8.0,76.4]
temp.append(3.4)
print(temp)

# list.clear() clears the list
# list.index(list item) gives the index of the item in the list
print(temp.index(3.4))

# the __method__ you see when you dir() aren't used that much. For example __getitem__ in list will get the item in the 
# list but its easier to just use list[index]
print(temp[1])

# Use [:] slice to get slices from the list
print(temp[0:2])
print(temp[2:]) #can omit the last or first index in slice to go till the end
temp[-1] #Gives the last item. Can also do slicing with negative indexing

# If there is a string inside a list you can get a character from the string using indexing
listnew=['hello',1,('damn','son')]
print(listnew[0][2]) #l from hello
print(listnew[2][0][2]) #m from damn
# dictionaries use keys instead of indexes to get the values

# you can convert from tuple to list and vice versa and also from a list to a dictionary provided the data is structured correctly
data = [["name", "John"], ["surname", "smith"]]
print(dict(data)) #type casted into dictionary


# Section 5
#creating own functions
def mean(mylist):
    '''Find mean of list of numbers'''
    meanval = sum(mylist)/len(mylist)
    return meanval #function with no return statement will return None which is also a data type
    # be careful about using print in the function instead of return. functionality is different

numlist = [2,4,6,7,8,9]
print(mean(numlist)) #calling mean and printing output

#conditionals
if 1<2 and 2<3: #Checks if the condition is True --> if True then print yes else no
    print('Yes')
else: #add elif for additional condition checks
    print('No')
# Can use and & or keywords in conditional for checking both or either conditions/

