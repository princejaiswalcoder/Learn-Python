print('''Program To Read A String And Display It In Reverse Order - Display one character per line.
Do not create a reverse string , just display in reverse order''')

string1 = input("Enter A String : 😎\n")
print("The",string1,"In Reverse Order Is : 👇")
length = len(string1)
for a in range(-1,(-length - 1),-1):
    print(string1[a])