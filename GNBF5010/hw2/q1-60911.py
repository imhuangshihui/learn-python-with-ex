'''
HW2-Q1-Unknown Letters
Author: HUANG Shihui
'''

unknown_letters=[]
nucleotides=['A', 'T', 'C', 'G']
with open('seqs.txt', 'r') as file:
    for seq in file:
        seq = seq.strip()  # remove whitespace characters
        for ch in seq:
            if ch not in nucleotides:
                unknown_letters.append(ch)
                only_once = list(set(unknown_letters))  # Use set to remove duplicates
    print(only_once)

