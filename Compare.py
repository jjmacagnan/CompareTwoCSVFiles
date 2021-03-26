f1 = open("metadata_mammoset.csv").readlines()
f2 = open("output_ddsm_all.csv").readlines()


file = open('output.csv', 'a')
for row1 in f1:
    # print(row1[:7])
    for row2 in f2:
        # print(row2[:7])
        if row1[:11] == row2[:11]:
            # print(row1)
            file.write(row2)
