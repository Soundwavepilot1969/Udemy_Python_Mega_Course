# Section 9
# List comprehension
#storing decimals is heavier compared to storing just int values so a lot of companies store int and later divide it by 10 or 100 to get the output.
temps = [221, 234, 340, 235, 334]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# the above can be done in a single line as follows:
new_temps_2 = [temp/10 for temp in temps]  #inline for loop used. This is faster
print(new_temps_2)

# List comprehension with if condition
new_temps_3 = [temp / 10 for temp in temps if temp>225] #remove 221
print(new_temps_3)

def foo(lst):
    return [integ for integ in lst if type(integ)==int] #returns only integers from a list

# adding if and else inside the inline for loop has to done like this where if and else comes before for ~ in ~
new_temps_4 = [temp/10 if temp>225 else 0 for temp in temps] #if temp>225 puts temp/10 else puts 0
print(new_temps_4)

def foo(lst):
    return sum(float(value) for value in lst) #sum of all items in list 
print(foo(['1.2','3.4','5.5']))

# section 10 - More about Functions
# some functions take one while others take more arguments
# Arguments are passed when function is called and parameters are defined when you define the function

#There are keyword argument and non-keyword arguments
    # non-keyword arguments/positional arguements --> function(4,5) when called
    # keyword arguments --> function(a=4,b=5) when called

# Default parameters are entered when defining the function
def function(a,b=5): #always non-default argument will follow default argument so cannot have function(a=4,b)
    return a+b

# you can pass n number of arguments into a function using *args. Here 'args' doesn't mean anything and can be 
# renamed as *sdfsd but naming convention is *args
def sumfn(*args):
    print(type(args))
    return sum(args) #args creates a tuple from all the arguments passed when calling the function
print(sumfn(1,2,3,4))

# sorted function can be used instead of calling sort method on the list

#Passing arbitrary number of key word arguments. above *args is for non-keyword arguments only for keyword args use **
def sumfn_2(**kwargs):
    print(type(kwargs)) #**kwargs creates a dictionary from all non-keyword arguments passed
    return sum(kwargs.values())

print(sumfn_2(a=1, b=2, c=3, e=4))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get) #max function allows iterable to be an argument. The dict.get method will return a value for key in dictionary else default

    