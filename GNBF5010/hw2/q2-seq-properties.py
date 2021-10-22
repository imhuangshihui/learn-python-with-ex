# GNBF5010 Homework 2 Question 2

import sys

MENU = '''
Please select the sequences property that you want to display, or press 0 to exit the program.
1) Total number of sequences
2) Number of pattern occurrences
3) Number of sequences with length >= min_len
4) Number of sequences with GC% >= min_GC
5) Number of sequences with length >= min_len and GC% >= min_GC
'''

PROMPT = "Enter the choice:"


def main():

    # load sequences to seqs list
    seqs = []
    filename = "seqs.txt"
    with open("seqs.txt", "r") as file:
        for line in file:
            line = line.rstrip().upper()
            seqs.append(line)
    #print(len(seqs))
    #print(seqs[0])
        
    # prompt menu for user to select
    print(MENU)
    choice = int(input(PROMPT))

    while (choice != 0):

        if choice == 1:
            # return totol number of seqs
            print(f"The total number of seqs are {len(seqs)}")

        elif choice == 2:
            # get patt from the user
            patt = input("Please enter your pattern: ")
            patt = patt.upper()
            
            # num of patt for each seq in seqs
            count = 0
            for seq in seqs:
                count += count_patt(seq, patt)
            print(count)

        elif choice == 3:
            min_len = int(input("Min len = "))
            count = 0
            for seq in seqs:
                if len(seq) >= min_len:
                    count += 1
            print(f"Number of seqs with len >= min_len is {count}.")

        elif choice == 4:
            min_gc = input("Min GC (e.g.50%) = ")
            count = 0
            # format user input, in case of percentage
            min_gc = format_gc(min_gc)                            
            for seq in seqs:
                gc = calc_gc(seq)
                if gc >= min_gc:
                    #print(gc)
                    count += 1
            print(f"Num of seqs with gc >= min_gc is {count}.")

        elif choice == 5:
            count = 0

            # get user inputs
            min_len = int(input("Min len = "))
            min_gc = input("Min GC (e.g.50%) = ")
            # format user input, in case of percentage
            min_gc = format_gc(min_gc) 

            for seq in seqs:
                gc = calc_gc(seq)
                if len(seq) >= min_len and gc >= min_gc:
                    count += 1
            print(f"Number of seqs with len >= min_len and gc >= min_gc is {count}.")

        elif choice != 0:
            print("Invalid input. Please enter again.")
            choice = int(input(PROMPT))
            
        print("\n==\n")

        # prepare for the next loop by asking for a new choice
        print(MENU)
        choice = int(input(PROMPT))

    print("Exiting the program ...")

    

def count_patt(s, pat):
    pos = 0
    cnt = 0
    len_patt = len(pat)
    while pos < len(s):
        substr = s[pos:(pos + len_patt)]
        if substr == pat:
            #print(substr)
            cnt += 1
            pos += len_patt
        else:
            pos += 1

    return cnt
    

def calc_gc(s):
    g_cnt = s.count("G")
    c_cnt = s.count("C")
    return float(g_cnt + c_cnt) / len(s) * 100


def format_gc(num_str):
    if '%' in num_str:
        ret = float(num_str.rstrip("%")) / 100
    else:
        ret = float(num_str)
    return ret


main()
