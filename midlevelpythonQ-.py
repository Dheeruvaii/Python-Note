""" randomize the list 
random.shuffle() function to shuffle the items and modify the original list. 
 random.sample() to randomize the items of a list and save them in a new list, rather than modifying the original list. 
"""
import random 
my_list=[1,2,3,4,5]
# new_list=random.shuffle(my_list)
new_list=random.sample(my_list,len(my_list) )
print(my_list)




# 2.Nonlocal statement to modify the outer_variable of the outer_function from within the inner_function.
def outer_function():

    outer_variable = 10

    def inner_function():

        nonlocal outer_variable

        outer_variable = 20  # Modify the variable in the enclosing scope

    inner_function()

    print("Outer variable:", outer_variable)  # Output: 20

outer_function()





# 3. Python to fetch every 3rd item from a list


my_list=[1,2,3,4,5]
new=my_list[::3] """define colon startting index and ending index"""
print(new)
