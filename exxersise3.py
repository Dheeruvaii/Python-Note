#no of guess 5
#print number of guess left
#after print game over
n=15
for i in range(1,10):
    print(f'you have {6-i} times to run   ')
    val=int(input("guess value: "))
    if(val==n):
        print("you predicted correct")
        break
    elif(val<n):
        print("predicted value is smaller than defined value")
    else:
        print("predicted value is bigger than deifened value")
    print("guess again")