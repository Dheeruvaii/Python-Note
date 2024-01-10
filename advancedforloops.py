# Tuples are sequences, just like lists. The difference between tuples and lists is that tuples are immutable; that is, they cannot be changed 
x= (10,20,30,40,50)
for var in x:
    print("index" + str(x.index(var))+ ":" ,var)




#  """tuble inside list call over a loop"""
x= [(10,20),(10,30),(20,30),(40,50)] 
for a,b in x:
    print(a,"plus",b,"plus",a+b)

# dictionary over for loops (python dictionary composed of key value pairs so in a-each loops we have to access each time key and value)
    stocks={
        "1":"2",
        "3":"4",
        "5":"6"
    }
    for key,value in stocks.items():
        print(key + ":" + str(value))


# strings (for loops can iterate through the each character  in a string)
        
    a=("dhiraj")
    for a in "dhiraj":
        print(a)