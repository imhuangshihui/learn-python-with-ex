filename = input("Enter file name: ")
try:
    fhand = open(filename)
except:
    print(f"{filename} can not be finded.")
    exit()

count = {}
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        mail = words[1]
        count[mail] = count.get(mail, 0) + 1
print(count)
