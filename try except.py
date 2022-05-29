from logging import exception


print("enter number a\n")
a=input()
print("enter number b\n")
b=input()
try:
    print("sum of these numbers is,int(a)+int(b)")
except exception as a:
    print(a)