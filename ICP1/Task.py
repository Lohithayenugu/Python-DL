import random
str1 = input("Please enter the input string")
str2 = input("Please enter the characters that are to be deleted with delimiter as space")
str2 = str2.split(' ')
for i in str2:
    str1 = str1.replace(i, '')
str1 = str1[::-1]
print(str1)

j=1
while(j):
    try:
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
        j=0;
    except ValueError:
        print('Non-numeric data found in the file.')



print("Adiition is:" , x+y)
print("Subtraction is:", x-y)
print("multiplication is:", x*y)
print("Division is:", x/y)
print("Modulus is:", x%y)

str2 = input("Please enter the input string")
str2 = str2.replace('python', 'pythons')
print(str2)
