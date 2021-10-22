'''
HW2-Q3-Average of tests
Author: HUANG Shihui
'''

# 1. Load all data to a dictionary
d = {}
with open('test1.txt', 'r') as f1:
    for l1 in f1:
        l1 = l1.split()
        d[l1[0]] = l1[1:]

with open('test2.txt', 'r') as f2:
    for l2 in f2:
        l2 = l2.split()
        if l2[0] not in d:
            d[l2[0]] = l2[1:]
        else:
            d[l2[0]] += l2[1:]

with open('test3.txt', 'r') as f3:
    for l3 in f3:
        l3 = l3.split()
        if l3[0] not in d:
            d[l3[0]] = l3[1:]
        else:
            d[l3[0]] += l3[1:]

# 2. calculate the ave of d
d_avg = {}
for key in d:
    L = len(d[key])
    total = 0
    for i in range(L):
        total += float(d[key][i])
    A = total / L
    d_avg[key] = A

# 3. output
with open('test_averages.txt', 'w') as output:
    output.write(f"{'Accession_Number'}\t{'Average value'}\n")
    for key,val in d_avg.items():
        output.write(key)
        output.write('\t')
        output.write(str(val))
        output.write('\n')
