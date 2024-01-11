
import pandas as  pd 

data = {'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Iterate over rows
for index, row in df.iterrows():
    print(row['Name'], row['Age'], row['City'])