filename = input("Enter file name: ")
try:
    fhand = open(filename)
except:
    print(f"{filename} isn't exit.")
    exit()

count = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

most_email = None
most_count = None
for key,val in count.items():
    if most_email is None or val > most_count:
        most_email = key
        most_count = val
print(most_email, most_count)
