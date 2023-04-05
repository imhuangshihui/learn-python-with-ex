from typing import List

with open('LQTS.known.genelist.txt', 'r') as f:
    genes: List[str] = [gene.rstrip() for gene in f]
    #print(genes)

output=open('step1.gt.QTgene.txt', 'w')

with open('step1.gt.txt', 'r') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.strip().split("\t")
        print(line[10])
        if line[10] in genes:
            #print("1")
            line.append("1")
        else:
            #print("0")
            line.append("0")
        line = '\t'.join(line)
        output.write(line + '\n')
