'''
HW2-Q4-Molecular weight
Author: HUANG Shihui
2021.10.14
'''

import string
alpha = string.ascii_lowercase
# Write a dict for amino_acid
amino_acid = {'A': 89, 'R': 174, 'N': 132, 'D': 133,
              'B': 133, 'C': 121, 'Q': 146, 'E':147,
              'Z': 147, 'G': 75, 'H':155, 'I': 131,
              'L': 131, 'K': 146, 'M': 149, 'F': 165,
              'P': 115, 'S': 105, 'T': 119, 'W': 204,
              'Y': 181, 'V': 117}

# Print out the sorted amino_acid by their weight
## Create a list of tuples of value-key pair
value_key_sorted = []
for k,v in amino_acid.items():
    value_key_sorted.append((v, k))
value_key_sorted.sort(reverse=True)
## Print nicely from highest to lowest frequency
### Create a (23, 3) list to store the frequency
row = 23
col = 3
amino_lst = []
for i in range(row):
    amino_lst.append([0] * col)
    amino_lst[i][0] = alpha[i] + '.'
amino_lst[0][1] = 'AA'
amino_lst[0][2] = 'MW'
### Add other element to this list
i = 1
for val,key in value_key_sorted:
    amino_lst[i][1] = key
    amino_lst[i][2] = str(val) + 'Da'
    i += 1
### Print out the list
for a,b,c in amino_lst:
    print(f"{a}\t{b}\t{c}")

# Calculate the molecular weight of the protein
with open("lysozyme.fasta", "r") as file:
    MW = 0
    for line in file:
        if line.startswith('>'):
            continue
        else:
            line = line.strip()
            for AA in line:
                if AA in amino_acid:
                    MW += amino_acid[AA]
    print(f"The molecular weight of lysozyme is: {MW}Da")

