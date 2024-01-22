
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
 
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, **kwargs):
		# access args index like array does
		self.speed = kwargs['s']
		self.color = kwargs['c']


# creating objects of car class
audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)

"""How do I access a module written in Python from C?"""
# Answer:

# Understanding how Python works is a given for any Python developer. However, there’s no point in trying to get a word-for-word answer. Instead, look out for personal stories on how candidates have used specific features. 

# You can get a pointer to the module object as follows:

# module = PyImport_ImportModule("");
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))