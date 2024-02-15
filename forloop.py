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



"""guess number game using range functions"""
    n = 15
for i in range(1, 6):
    print(f'You have {6-i} guesses left.')
    guess = int(input("Guess the number: "))
    if guess == n:
        print("Congratulations! You guessed it right!")
        break
    elif guess < n:
        print("The guessed number is smaller than the target number.")
    else:
        print("The guessed number is greater than the target number.")
else:
    print("Game Over! You ran out of guesses.")