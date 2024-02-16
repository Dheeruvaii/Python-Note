# using with statement
with open('myfile.txt', 'w') as file:
    file.write('DataCamp Black Friday Sale!!!')


    with open("dheeru.txt",'w') as file:
        file.write("Backend developer")

with open("dheeru.txt",'r') as file:
    file.read()
    print(file)