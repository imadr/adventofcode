from rich.console import Console

console = Console()

topo = """0123
1234
8765
9876"""

gradient = [[212, 242, 255], [192, 232, 255], [172, 222, 255], [152, 212, 253], [132, 202, 243], [112, 182, 233], [92, 162, 223], [72, 142, 203], [51, 122, 183], [51, 102, 153]]

topo = [list(map(int, line)) for line in topo.split("\n")]

def recursive_search(row, column, path):
    cell = topo[row][column]
    n1 = [-1, -1]
    n2 = [-1, -1]
    n3 = [-1, -1]
    n4 = [-1, -1]
    if row < len(topo)-1:
        n1 = [row+1, column]
    if row > 0:
        n2 = [row-1, column]
    if column < len(topo[0])-1:
        n3 = [row, column+1]
    if column > 0:
        n4 = [row, column-1]

    if topo[n1[0]][n1[1]] - cell == 1:
        return recursive_search(n1[0], n1[1], path+[[row, column], n1])
    if topo[n2[0]][n2[1]] - cell == 1:
        return recursive_search(n2[0], n2[1], path+[[row, column], n2])
    if topo[n3[0]][n3[1]] - cell == 1:
        return recursive_search(n3[0], n3[1], path+[[row, column], n3])
    if topo[n4[0]][n4[1]] - cell == 1:
        return recursive_search(n4[0], n4[1], path+[[row, column], n4])
    return path

for row in range(0, len(topo)):
    for column in range(0, len(topo[row])):
        cell = topo[row][column]
        color = ','.join(map(str, gradient[cell]))
        console.print(f"[rgb("+color+")]"+str(cell)+"[/rgb("+color+")]", end="")
    console.print()

print(recursive_search(0, 0, []))
# for path in :
#     print(topo[path[0]][path[1]], end="")