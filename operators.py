#asssigned operators
#comparison operators
#identity operators
#membership operators
#bitwise operators
  #arithmetic operators
#print("5 + 6 is",5+6)
#print("5 ** 3",5**3)
# assigned operators
#X=4
#print(X)
#X +=3
#print(X)
  #COMPARISON OPERATORS
#v = 5
#print(v <= 8)
  #loGICAL
#a=True
#b=False
#print(True and False)
  #identity operators
#print(5 is not 6)
#print(6 is 6)
  #membership operators
#List= [1,2,3,5,6]
#print(type(List))
#print(34 not in list)
   #BITwiSE OPERAtors
print(0 | 3)
print(0 & 3)


import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Iterate over rows
for index, row in df.iterrows():
    print(row['Name'], row['Age'], row['City'])
