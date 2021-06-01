#5 no Question :


list1 = []
list2 = []
result = False
length1 = int(input("Enter length of the list 1 : "))


for i in range(length1):
    n = float(input("Value [" + str(i+1) + "] :"))
    list1.append(n)

print("The 1st list is : ", list1)

length2 = int(input("Enter length of the list 2 : "))

for i in range(length2):
    m = float(input("Value [" + str(i+1) + "] :"))
    list2.append(m)

print("The 2nd list is : ", list2)

for i in list1:
    for j in list2:
        if i == j:
            result = True

print(result)