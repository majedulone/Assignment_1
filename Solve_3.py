#3 no Question :

list = []

length = int(input("Enter length of the list : "))

for i in range(length):
    n = float(input("Value [" + str(i+1) + "] :"))
    list.append(n)

print("The list is : ",list)
print("The largest number of the list is : ", max(list))

