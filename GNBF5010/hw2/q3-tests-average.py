# Homework 2 Question 3

# This script was modified from homework submission of a student.

import re
import sys

OUT_FILE = 'test_averages.txt'

# Given a list of experiment result filenames, parse each file and return
# a dictionary with accession number as key and list of number as value.
def parse(filenames):
    
    # A function takes a line and returns the accession number and a 
    # list of numbers
    def parse_line(line):
        key = value = None
        fields = re.split(r'\s+', line.rstrip())
        if len(fields) >= 2:    # Check record has value or not
            key = fields[0]
            value = [ float(num) for num in fields[1:] ]
        return key, value

    # Parse line by line for each data files
    result = {}
    for fn in filenames:
        with open(fn, 'r') as infile:
            for line in infile:
                # Split line by whitespace including tab (\t)
                k, v = parse_line(line)
                if k is not None:
                    result[k] = result.get(k, []) + v
    return result


# Main Routine
def main():

    # Parse all data from input file(s) to a dict.
    gene_data = parse(['dat/test1.txt', 'dat/test2.txt', 'dat/test3.txt'])

    # Calculate the average value of each gene in the dict.
    result = {acc:sum(values)/len(values) for acc,values in gene_data.items()}

    # Write the average of each gene to the output file
    with open(OUT_FILE, 'w') as outfile:
        outfile.write('\n'.join(
            [f'{acc_num}\t{avg:.4f}' for acc_num, avg in result.items()]
        ))

    print(f'Parsed result is written to file "{OUT_FILE}" successfully.')


# Run the main routine
main()