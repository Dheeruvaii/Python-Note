for num in range(2, 23):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    else:
        if prime:
            print(num)



def prime(x,y):
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