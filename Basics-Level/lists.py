


list1 = [1,2,2,4,6,8]
print(list1) 
print(8 in list1)
if 8 in list1:
      print("yes its in the list")
#     2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""concatinate list"""

lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']
lst3 = [x + y for x, y in zip(lst1, lst2)]
print(lst3)