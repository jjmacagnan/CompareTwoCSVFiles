f1 = open("tests1.csv").readlines()
f2 = open("tests2.csv").readlines()


file = open('edge_histogram.csv', 'a')
for row1 in f1:
    # print(row1[:7])
    for row2 in f2:
        # print(row2[:7])
        if row1[:19] == row2[:19]:
            # print(row1)
            file.write(row2)
