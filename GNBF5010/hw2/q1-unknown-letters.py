#
# Homework 2 - Question 1 (Unknown letters)
# This program list which letters in the data file are not A,T,C or G.
#

def main():
    
    # Read sequences from seqs.txt and 
    # use a list to store sequences in the file
    seqs = []
    with open("seqs.txt") as fh:
        for line in fh:
            line = line.rstrip()
            seq = line.upper()
            seqs.append(seq)
            
    # Use two for-loops to scan letters in each sequence
    # Create a list to store unknown letters
    unknown_letters = []
    for seq in seqs:
        for letter in seq:
            if letter not in 'ATCG' and letter not in unknown_letters:
                unknown_letters.append(letter)
                
    # print output
    print(sorted(unknown_letters))
            
    
main()
