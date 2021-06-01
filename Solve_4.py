#4 no Question :

f_list = []

length = int(input("Enter length of the list : "))

for i in range(length):
    n = float(input("Value [" + str(i+1) + "] :"))
    f_list.append(n)

print("The list is : ",f_list)
f_list = list(set(f_list))
print("The list without Duplicate values is : ", f_list)