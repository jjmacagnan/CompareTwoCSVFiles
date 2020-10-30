f1 = open("metadata_DDSM.csv").readlines()
f2 = open("ddsm_all.csv").readlines()


file = open('ddsm.csv', 'a')
for row1 in f1:
    # print(row1[:7])
    for row2 in f2:
        # print(row2[:7])
        if row1[:15] == row2[:15]:
            # print(row1)
            file.write(row2)
