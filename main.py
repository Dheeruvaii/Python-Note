# break and continue
q=0
while(True):
    if q+1<5:
        q= q + 1
        continue
    print(q+1,end ="")
    if(q==20):
        break
    q=q+1 
# conditionsl 
    var1 = 23
var2 = 55
var3 = (input())

if (var3>var2):
      print("greater")
elif var3==var2:
      print("equal")
else:
      print("lesser")


# practice
      D={'dhiraj':'100.100.100',
   'cage':'200.200.200',
   'ram':'300.300.300',
   'hoby':'12345'
   } 
key=input("enter name:")
A=key.capitalize()
print(D)
print([A])


# set
c = set()
print(type(c))
s_from_list=set([1, 2, 3, 4, 4, 5])
print(s_from_list)
print(type(s_from_list))
c.add(8)
c.add(4)
s1=c.union({1,8,3})
print(c,s1)


# shorthandif
a =int(input("enter a\n"))
b= int(input("enter b\n"))

#if a>b: print("a is big")
print("a is bigger than b ") if a>b else print("b is bigger than a" )



# try except

from logging import exception


print("enter number a\n")
a=input()
print("enter number b\n")
b=input()
try:
    print("sum of these numbers is,int(a)+int(b)")
except exception as a:
    print(a)
  

#   write and appernd
F =open("dheeru.txt","w")
F.write("im god")
F.closed()