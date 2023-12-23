list1=[ ["dheeruvaii",10], ["harry",12], ["ram",13], ["shyam",23]]
dict1=dict(list1)
for item,pen in list1:
    print(item, "sex for",pen)





    
age=int(input("enter your valid age"))
if age>18:
    print("you can drive")
elif age==18:
    print("we will think about you")
else:
    print("you cannot drive")