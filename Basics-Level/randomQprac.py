
"""sort a list elements"""

my_list=[1,2,3,6,5]
my_list.sort()
my_list.remove(2)
my_list.pop(2)
print(my_list)

"""reverse a string"""
str1 = "Analytics Vidhya"
str2 = ""
for i in str1:
    str2 = i + str2
print("The original string is: ", str1)
print("The reversed string is: ", str2)



"""remove a file"""
# import os
# os.remove("txt1.txt")
