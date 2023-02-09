print("Write a program to input a list and an element , and remove all occurence of the given element from the list .")

lst = eval(input("Enter a list :"))
elem_rem = eval(input("Enter the element to be removed :"))
c = lst.count(elem_rem)
if  c == 0:
    print("Item Not In The List")
else:
    while c > 0:
        i = lst.index(elem_rem)
        lst.pop(i)
        c -= 1

print("After removing",lst)