f1 = open("mass_case_description_test_set.csv").readlines()
f2 = open("output_ddsm_all.csv").readlines()


file = open('output_mass_test_set.csv', 'a')
for row1 in f1:
    # print(row1[:7])
    for row2 in f2:
        # print(row2[:7])
        if row1[:15] == row2[:15]:
            # print(row1)
            file.write(row2)
