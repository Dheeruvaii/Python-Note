#EX 2(faulty calculator)
print(" enter your first number")
A= int(input())
print("Enter your second Number")
B= int(input())
print('What operation do you want:+, -, * or ÷ ?')
C=input()
if A==45 and B==3 and C =='*':
    print("answr is 555")
elif A==56 and B==9 and C=='+':
    print("answer is 77" )
elif A==56 and B==6 and C=='/':
    print("4")
elif C=='*':
    multiplication=A*B
    print("multiplication")
elif C=='+':
    add=A+B
    print("add")
elif C=='-':
    sub=A-B
    print("sub")
elif C=='%':
    percentage=A%B
    print("percent")
else:
    print(" do more practise")

