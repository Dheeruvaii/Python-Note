var1 = 7
var2 = 2
result = var1 // var2+ var1%var2
print(result)

def test(x, y=[]):
	y.append(x)
	return y
print(test(1))
print(test(2))
name = input("Input your name: ")
if name == "John" or "Brian":
	print("Welcome, John or Brian!")
else:
	print("You're not John or Brian.")

import array
a = array.array('i', [1, 2, 3])
for i in a:
    print(i, end=' ')    #OUTPUT: 1 2 3
a = array.array('i', [1, 2, 'string'])    #OUTPUT: TypeError: an integer is required (got type str)
a = [1, 2, 'string']
for i in a:
   print(i, end=' ') 