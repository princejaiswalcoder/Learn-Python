print("Program that prints the following pattern without using any nested loop")
print('''
Pattern 👇
#
##
###
####
#####
''')
string = "#"
pattern = ""
for a in range(5):
    pattern += string
    print(pattern)