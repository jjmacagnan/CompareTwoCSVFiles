import os

original_files_path = 'original_files'
compared_files_path = 'compared_files'

f1 = open("OR_test_metadata_mammoset_ddsm_pathology_class_6.csv").readlines()

files = os.listdir(original_files_path)

for filename in files:
    # print(filename)

    if not filename.startswith('.'):
        print(filename)

        f2 = open(original_files_path + "/" + filename).readlines()

        output_file = open(compared_files_path + "/" + filename, 'w')
        for row1 in f1:
            # print(row1[:7])
            for row2 in f2:
                # print(row2[:7])
                if row1[:16] == row2[:16]:
                    # print(row1)
                    output_file.write(row2)

        output_file.close()
