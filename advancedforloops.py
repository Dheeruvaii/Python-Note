# Tuples are sequences, just like lists. The difference between tuples and lists is that tuples are immutable; that is, they cannot be changed 
x= (10,20,30,40,50)
for var in x:
    print("index" + str(x.index(var))+ ":" ,var)


y=(20,30,40,50,60)
for i in y :
    print("index" + str(y.index(var))+ ":",i)



#  """tuble inside list call over a loop"""
x= [(10,20),(10,30),(20,30),(40,50)] 
for a,b in x:
    print(a,"plus",b,"plus",a+b)

# dictionary over for loops (python dictionary composed of key value pairs so in a-each loops we have to access each time key and value)
    # stocks={
    #     "1":"2",
    #     "3":"4",
    #     "5":"6"
    # }
    # for key,value in stocks.items():
    #     print(key + ":" + str(value))
    dict={
        "name":"dhiraj",
        "address":"nepal",
        "work":"developer"
    }
    for key ,value in dict.items():
        print(key +  ":" + str(value))


# strings (for loops can iterate through the each character  in a string)
        
    a=("dhiraj")
    for a in "dhiraj":
        print(a)


# # common python loops over python packages  like numpy array  
import numpy as np 
np.random.seed(10)  
x=np.random.randint(10,size=10)
y=np.random.randint(10,size=6)
for value in x:
    print(value)
#     # one dimensional array

#     # crate a two dimensional array 

    import numpy as np
    np.random.seed(0)
    x=np.random.randint(10,size=6)
    y=np.random.randint(10,size=6)
    z=np.array([x,y])
    for val in np.nditer(z):
        print(val)

import numpy as np
np.random.seed(9)
x=np.random.randint(10,size=6)
y=np.random.randint(10,size=6)
for value in  x,y:
    print(x,y)
# workflow of for loops over pandas DataFrames
    
import pandas as pd 
import csv 
data = [
    ["Country", "Capital", "GDP ($US Trillion)", "Population"],
    ["Ireland", "Dublin", 0.3337, 4784000],
    ["United Kingdom", "London", 2.622, 66040000],
    ["United States", "Washington, D.C.", 19.39, 327200000],
    ["China", "Beijing", 12.24, 1386000000],
    ["India", "New Delhi", 2.597, 1339000000],
    ["Germany", "Berlin", 3.677, 82790000]
]

def save_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

        
def main():
    file_path = 'gdp.csv'
    save_to_csv(file_path, data)
    print(f'Data has been saved to {file_path}')

if __name__ == "__main__":
    main()

import pandas as pd 
import csv


personal_data= [
                ["Name","address" ,"professions"],
                [
                    "Dhiraj","Surkhet","Backenddeveloper"
                ]
]
def save_to_csv(file_path,personal_data):
    with open(file_path, 'w' ,newline ='') as file:
        write_file=csv.writer(file)
        write_file.writerows(personal_data)
def main():
    file_path="personal_informations.png"
    save_to_csv(file_path,personal_data)
    print(file_path)

if __name__=="__main__":
    main()

        # df=pd.read_csv('gdp.csv',index_col=0)
        # for val in df:
        #     print(val)
        #     for label ,row in df.iterrows():
        #         print(label + "+" + row[''])
# the range functions lets see how can we use loops to iterate over any data structure/sequences
    # three eays to call range()
    # range(stop)
    # range(st,stop)
    # range(start,stop,step)
    # go with one by one

#     for i in range(3):
#         print(i)

#     languages=[['a','b'],['p','j']]
#     for x in languages:
#         print("------")
#         for lang in x:
#             print(lang)
# #   continue and break for a loo[LookupError]
#             for c in languages:
#                 for d in c:
#                     if d=="p":
#                         continue
#                     print(d)
# #  continue and break continue
                    
#                     from math import sqrt
#                     number=0

#                     for i in range(10):
#                         number= i**2
#                         if i:
#                             continue
#                         print(str(round(sqrt(number)))+'square' + str(number))


#                     number=0
#                     for i in range(10):
#                         number=i ** 2

#                         if i == 7:
#                             break

#                         print(str(round(sqrt(number)))+'squard is equals to'+str(number))

