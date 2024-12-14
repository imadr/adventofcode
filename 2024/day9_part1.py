disk_map = """233313312141413140211"""
files = []

is_file = True
file_id = 0
for c in disk_map:
    if is_file:
        files += [str(file_id)]*int(c)
        file_id += 1
    else:
        files += ["."]*int(c)
    is_file = not is_file

files_len_range = reversed(range(0, len(files)))
files = list(files)
while True:
    done = False
    for i in files_len_range:
        if "." in files:
            ii = files.index(".")
            if ii >= i:
                done = True
                break
            elif files[i] != ".":
                files[files.index(".")] = files[i]
                files[i] = "."
        else:
            done = True
            break

    if done:
        break

checksum = 0
for i in range(0, len(files)):
    if files[i] == ".":
        break
    checksum += int(files[i])*i
print(checksum)