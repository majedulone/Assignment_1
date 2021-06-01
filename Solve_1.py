#1 no Question :

m = str(input("Enter a String : "))

if len(m) < 2:
    print("Empty String")
else:
    x = m[0:2]
    y = m[-2:]
    print(x + y)
exit(0)
