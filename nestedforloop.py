# for print rows(*)
rows=5
column=3
for i in range(rows):
    for j in range(column):
        print('*',end='')
    print('')



# # While Loop inside list nested loop
# names=['A','B','C']

# for name in names:

#     count= 0
#     while count < 5:
#         print(name, end='')
#         count = count + 1

#     print()
# single line nested loops using list comphrehensions
# a=['A','B','C']
# b=['D','E','F']

# final=[]
# for i in a:
#     for j in b:
#         final.append(i+j)
        
#     print(final)


# using single line
a= [2, 3, 4]
b= [3, 5, 6]
for i in a:
    for j in b:
        if i == j:
            break

            continue
        print(i,'*' ,j,'=',i*j)

# final= [i+j for i in a  for j in b]
# print(final)

a= [1, 2, 3], [4, 5, 6]
count=0
for i in a:
    for j in i:
        print('iterations',count,end=':')
        print(j)
        count=count+1