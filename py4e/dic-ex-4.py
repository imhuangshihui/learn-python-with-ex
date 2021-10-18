'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

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
