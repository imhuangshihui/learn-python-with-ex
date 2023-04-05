# cat step23456.filter.file | head -100 > annovar.txt
# cat gt.txt | head -100 > gatk.vcf
# The number of output file annovar.withID.txt even less than the number of variant in gatk.vcf
f1 = open('annovar.txt', 'r')
anno = f1.readlines()
f2 = open('annovar.withID.txt', 'w')
with open('gatk.vcf', 'r') as f3:
    lines = f3.readlines()
    for line in lines:
        if line.startswith("##")
        line = line.strip().split('\t')
        # print(line[2])
        for var in anno:
            pos = var.strip().split('\t')
            if line[1] in pos[1]:
                if len(line) == 3:
                    f2.write(var.strip())
                    f2.write('\t')
                    f2.write(str(line[2]) + '\n')
                else:
                    f2.write(var.strip() + '\n')
f1.close()
f2.close()



