filename = input("Enter a file name: ")
try:
    fhand = open(filename)
except:
    print(f"{filename} isn't exit. ")
    exit()

count = {}
for line in fhand:
    if line.startswith('From'):
        line = line.split()
        add = line[1]
        add = add.split('@')
        count[add[1]] = count.get(add[1], 0) + 1
print(count)
