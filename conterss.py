k = open("zScore.csv").readlines()

for i in k:
    p = i.split(",")
    print(len(p))