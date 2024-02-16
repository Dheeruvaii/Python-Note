
import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
add_data ={'NewName':['Alice']}

new={'data':df}
new.update({"add_data":pd.DataFrame(add_data)})
for index, row in df.iterrows():
    print(row['Name'], row['Age'], row['City'])

print(new["add_data"])
# import pandas as pd

# data = {'Name': ['John', 'Jane', 'Mike'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'London', 'Paris']}

# df = pd.DataFrame(data)

# # Existing dictionary
# existing_data = {"existing_data": "some_value"}

# # Append DataFrame to the existing dictionary
# existing_data.update({"new_data": df})

# # Iterate over rows
# for index, row in df.iterrows():
#     print(row['Name'], row['Age'], row['City'])
