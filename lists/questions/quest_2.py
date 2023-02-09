print("Program to calculate the mean of a given list of numbers .")

lst = eval(input("Enter a list :"))
length = len(lst)
mean = sum(lst) / length
print(mean,"is the mean of given",lst)