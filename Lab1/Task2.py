n=int(input("Enter the number of records"))
list=[]
dict={}
for i in range(n):
    print("Record "+str(i+1)+" : ")
    name=str(input("Enter name "))
    subject = str(input("Enter subject "))
    j = 1
    while (j):
        try:
            marks=float(input("Enter marks "))
            j = 0
        except ValueError:
            print('Non-numeric data.')
    list.append((name,(subject,marks)))
print("\nEntered input data")
print(list)
for i in list:
    if i[0] in dict:
        dict[i[0]].append(i[1])
    else:
        dict[i[0]]=[i[1]]
print("\n----------------------------------------------------------------------\n")
print("Data stored in dictionary\n")
print(dict)
