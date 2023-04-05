with open('annovar.withID.DN.txt', 'r') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.strip().split('\t')
        diag = line[-1].strip().split(',')
        #print(diag)
        apcount = 0
        nonap = 0
        for i in diag:
            if i == ".":
                continue
            else:
                if i == "ApHCM":
                    apcount += 1
                else:
                    nonap += 1
        print(apcount, end='\t')
        print(nonap)

