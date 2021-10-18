filename = input("Enter the file name: ")
try:
    fhand = open(filename)
except:
    print("File cannot be opened:", filename)
    exit()

count = {}
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) >= 3:
        days = words[2]
        count[days] = count.get(days, 0) + 1
    else:
        continue
print(count)


