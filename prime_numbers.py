for num in range(2, 23):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    else:
        if prime:
            print(num)