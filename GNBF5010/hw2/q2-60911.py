'''
HW2-Q2-Sequence Properties
Author: HUANG Shihui
'''

def seq_num1():
    print("Total number of sequence is: ", len(seqs))

def spe_seq_num2():
    with open('seqs.txt', 'r') as seq_file:
        d = seq_file.read()
        inp = input("The target sequence: ")
        occur = d.count(inp)
    print("Number of pattern occurrences is: ", occur)

def seq_len3():
    count = 0
    inp = int(input("min_len = "))
    for seq in seqs:
        if len(seq) >= inp:
            count += 1
    print("Number of sequences with length >= %d: %d" % (inp, count))

def GC4():
    total_seq = 0
    inp = int(input("min_GC (e.g. 50%) = "))
    for seq in seqs:
        num_of_GC = 0
        for ch in seq:
            if ch=="G" or ch=="C":
                num_of_GC += 1
        GC_content = (num_of_GC / len(seq)) * 100
        if float(GC_content) >= float(inp):
            total_seq += 1
    print("Num of seqs with gc >= %d%% is: %d" % (inp, total_seq))

def combine5():
    count=0
    inp1 = int(input("min_len = "))
    inp2 = int(input("min_GC (e.g. 50%) = "))
    for seq in seqs:
        num_of_GC = 0
        for ch in seq:
            if ch=="G" or ch=="C":
                num_of_GC += 1
        GC_content=(num_of_GC/len(seq)) * 100
        if float(GC_content) >= float(inp2) and len(seq) >= inp1:
            count += 1
    print("Number of seqs with len >= %d and gc >= %d%% is %d " % (inp1, inp2, count))

seqs=[]
def main():
    with open('seqs.txt', 'r') as seq_file:
        for line in seq_file:
            line = line.strip()
            seqs.append(line)
    while True:  # show the menu
        print()
        print("="*20)
        print("Please select the sequences property that you want to display, or press 0 to exit the program.")
        print("1) Total number of sequences")
        print("2) Number of pattern occurrences")
        print("3) Number of sequences with length >= min_len ")
        print("4) Number of sequences with GC% >= min_GC")
        print("5) Number of sequences with length >= min_len and GC% >= min_GC\n")
        inp = input("Enter the choice: ")
        try:
            if inp=="1":
                seq_num1()
            elif inp=="2":
                spe_seq_num2()
            elif inp=="3":
                seq_len3()
            elif inp=="4":
                GC4()
            elif inp=="5":
                combine5()
            elif inp=="0":
                print("Exiting...")
                break
        except ValueError:
            print("Invalid input!")

if __name__ == '__main__':
    main()



