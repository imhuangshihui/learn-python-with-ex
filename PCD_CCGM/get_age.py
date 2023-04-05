from typing import List

with open('pcdpatients.txt', 'r') as f1:
    patient: List[str] = [p.rstrip() for p in f1]

outfile = open('age_pcd.txt', 'w')

with open('age_stroke.tsv', 'r') as f2:
    lines = f2.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        else:
            line = line.rstrip().split('\t')
            if line[0] in patient:
                outfile.write(line[0] + '\t' + line[1])
                outfile.write('\n')
outfile.close()


