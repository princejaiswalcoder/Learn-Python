print("Write a program that reads email id of a person in the form of s string and ensures that it belongs to domain @gmail.com")
email = input("Enter Email Id :")
domain = "@gmail.com"
if domain == email:
    print("write proper email 😂")
elif domain in email:
    print("it belongs to @gmail.com 😍")
else:
    print("It belongs to another provider 👿")