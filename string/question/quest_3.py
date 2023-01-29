print("Write A Program To Input A String And Check If It Is A Palindrome String Using A String Slice")
palin = input("Enter A String , To Check Palindrome 😲: \n")
if palin == palin[::-1]:
    print(f"{palin} is a palindrome 🏆")
else:
    print(f"{palin} is not a palindrome 👿")
