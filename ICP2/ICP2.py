n = int(input("Enter number of elements"))
list1=[]
list2=[]
for x in range(n):
    list1.append(float(input("Enter "+str(x+1)+" element")))
list2 = [x * 0.454 for x in list1]
print("L1: ",list1)
print("Output: ",list2)
def string_alternative():
    str= input("Enter the string")
    str1 = ""
    for i in range(len(str)):
        if(i%2==0):
            str1=str1+str[i]
    print(str1)
string_alternative()
Dict = {}
file_name=input("Enter the file name")
f=open(file_name, "r")
contents=f.readlines()
for z in contents:
    if(z.endswith("\n")):
        z=z[0:len(z)-1]
    line=z.split(" ")
    for y in line:
        if y in Dict:
            Dict[y]=Dict[y]+1
        else:
            Dict[y]=1

file_name_dest = input("Enter the destination file name")
f=open(file_name_dest, "w+")
for i in Dict:
     f.write(i+" : "+str(Dict[i])+"\n")
f.close()
print(Dict)
