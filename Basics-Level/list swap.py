#  Find the length of the list and simply swap the first element with (n-1)th element.

# def swaplist(list):
#     first=list.pop(0)
#     last=list.pop(-1)

#     list.insert(0,last)
#     list.append(first)
#     print(swaplist)
#     return list

# new_list=[12,13,14,15,16]
# print(swaplist(new_list))
 
num=[1,2,3,4,5]
print(*num)
# num=num+1
# print(**num)

def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")