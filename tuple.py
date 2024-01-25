# mytuple = ("apple", "banana", "cherry")
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))



def prime(x,y):
    """
     using func"""
    prime=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                prime.append(i)
    return prime
a=2
b=7
lst=prime(a,b)
if len(lst) == 0:
    print('not prime'
          )
else:
    print('prime',lst)

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark() 
    
# class Human:
#     def __init__(self,name):
#         self.name=name
#     def intelligent(self):
#         print(f"{self.name}")

# human_beings=Human
# human_beings.intelligent()
