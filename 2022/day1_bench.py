import timeit

print(min(timeit.repeat(repeat=50, number=100, stmt=r"""a = max([sum([int(y) for y in x.split("\n")]) for x in open("input.txt").read().split("\n\n")])""")))