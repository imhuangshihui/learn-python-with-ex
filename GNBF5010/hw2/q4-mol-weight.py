# Homework 2 Question 4

# This program constructs a dictionary of 
# amino acids codes and their corresponding 
# molecular weights for calculating the 
# molecular weight of input protein.

aa_mol_weight = {
    'A': 89,
    'R': 174,
    'N': 132,
    'D': 133,
    'B': 133,
    'C': 121,
    'Q': 146,
    'E': 147,
    'Z': 147,
    'G': 75,
    'H': 155,
    'I': 131,
    'L': 131,
    'K': 146,
    'M': 149,
    'F': 165,
    'P': 115,
    'S': 105,
    'T': 119,
    'W': 204,
    'Y': 181,
    'V': 117
}

def main():
    # Use a temp list to store the value-key
    # pairs in the dictionary.
    tmp = []
    for i, j in aa_mol_weight.items():
        tmp.append((j, i))

    # Print the dictionary in the descending
    # order of molecular weights.    
    print('AA', '\t', 'MW')
    for g in sorted(tmp, reverse = True):
        print(g[1], '\t', g[0], 'Da', sep = '')
        
    with open('lysozyme.fasta', 'r') as infile:
    
        # Calculate the total molecular weight
        # of the input protein.
        w = 0
        for line in infile:
            if line[0] != '>':
               line = line.strip()
               for j in line:
                   w += aa_mol_weight[j]
    
    print()
    print('The molecular weight of lysozyme is:', w)

main()