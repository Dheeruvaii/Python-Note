# This is a global variable
x = 10
def func():
    # This is a local variable
    x = 5
    print(x)
func()
print(x)