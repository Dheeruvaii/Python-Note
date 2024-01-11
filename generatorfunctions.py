# generator func is a normal functions with yield 

def simpleGeneratorFunc():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFunc():
    print(value)