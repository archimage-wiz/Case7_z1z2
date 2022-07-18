from pprint import pprint

file1 = "sorted/1.txt"
file2 = "sorted/2.txt"
file3 = "sorted/3.txt"

files_list = [file1, file2, file3]

files_dict = {}

# задача №3

for file in files_list:
    with open(file, encoding="UTF-8") as cfile:
        lines_list = []
        for line in cfile:
            lines_list += [line.strip()]
        files_dict[len(lines_list)] = [file, lines_list]

sorted_by_lines = sorted(list(files_dict.keys()))
#pprint(files_dict)

with open("sorted/out.txt", "w", encoding="UTF-8") as cfile:
    for current_index in sorted_by_lines:
        cfile.write(files_dict[current_index][0] + "\n")
        cfile.write(str(current_index) + "\n")
        for line in files_dict[current_index][1]:
            cfile.write(line + "\n")
        #cfile.write("\n")


