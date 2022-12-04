input_ = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

count = 0
input_ = [x.split(",") for x in input_.split("\n")]
for i in input_:
    elf_1 = [int(x) for x in i[0].split("-")]
    elf_2 = [int(x) for x in i[1].split("-")]
    print(elf_1)
    print()