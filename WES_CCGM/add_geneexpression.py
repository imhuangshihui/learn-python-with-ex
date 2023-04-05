import re

a = open("a.txt", "w")
b = open("b.txt", "w")
g = open("g.txt", "w")
others = open("o.txt", "w")

with open("cogtest.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        temp = line.strip().split('\t')
        gene_list = temp[-1]
        gene = gene_list.split(";")
        #print(gene)
        for i in gene:
            if re.match(r"PCDHG\S", i):
                g.write(line)
            elif re.match(r"PCDHA\S", i):
                a.write(line)
            elif re.match(r"PCDHB\S", i):
                b.write(line)
            elif re.match(r"\d", i) or i not in "PCDH":
                others.write(line)

a.close()
b.close()
g.close()
others.close()
# Remove the duplicate lines
nonpcd_seen = set() # holds lines already seen
non = open("non_pcdh.txt", "w")
for line in open("o.txt", "r"):
    if line not in nonpcd_seen: # not a duplicate
        non.write(line)
        nonpcd_seen.add(line)
non.close()

pcdha_seen = set() # holds lines already seen
outa = open("pcdha.txt", "w")
for line in open("a.txt", "r"):
    if line not in pcdha_seen: # not a duplicate
        outa.write(line)
        pcdha_seen.add(line)
outa.close()

pcdhb_seen = set() # holds lines already seen
outb = open("pcdhb.txt", "w")
for line in open("b.txt", "r"):
    if line not in pcdhb_seen: # not a duplicate
        outb.write(line)
        pcdhb_seen.add(line)
outb.close()

pcdhg_seen = set() # holds lines already seen
outg = open("pcdhg.txt", "w")
for line in open("g.txt", "r"):
    if line not in pcdhg_seen: # not a duplicate
        outg.write(line)
        pcdhg_seen.add(line)
outg.close()
