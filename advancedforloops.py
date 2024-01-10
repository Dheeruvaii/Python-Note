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


# common python loops over python packages  like numpy array  
import numpy as np 
np.random.seed(0)  
x=np.random.randint(10,size=6)
y=np.random.randint(10,size=6)
for value in x:
    print(value)
    # one dimensional array

    # crate a two dimensional array 

    import numpy as np
    np.random.seed(0)
    x=np.random.randint(10,size=6)
    y=np.random.randint(10,size=6)
    z=np.array([x,y])
    for val in np.nditer(z):
        print(val)

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


        # df=pd.read_csv('gdp.csv',index_col=0)
        # for val in df:
        #     print(val)
        #     for label ,row in df.iterrows():
        #         print(label + "+" + row[''])
