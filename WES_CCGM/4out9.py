from collections import Counter
with open('final.test.txt', 'r') as f:
    lines = f.readlines()
    # score = []
    pred = ["D", "P", "A", "M", "H"]
    for line in lines:
        line = line.strip().split("\t")
        score = [line[46], line[49], line[55], line[58], line[61], line[64], line[67], line[72], line[78]]
        # print(score)
        temp = dict(Counter(score))
        print(temp)
        # for k in temp:
        #     if k == "D" and temp[k] >= 4:
        #         print("D_Mis")
        #     else:
        #         print("non_D_Mis;NA")

