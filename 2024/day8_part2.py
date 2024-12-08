s = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split("\n")[1:]

m = [list(x) for x in s]

antennas_frequencies = {}

for row in range(0, len(m)):
    for column in range(0, len(m[0])):
        cell = m[row][column]
        if cell != ".":
            if cell in antennas_frequencies:
                antennas_frequencies[cell].append([row, column])
            else:
                antennas_frequencies[cell] = [[row, column]]

antinodes = []
for frequency in antennas_frequencies:
    antennas = antennas_frequencies[frequency]
    for i in range(0, len(antennas)):
        for j in range(0, len(antennas)):
            if i == j:
                continue
            out_of_bounds = False
            delta = [antennas[i][0]-antennas[j][0], antennas[i][1]-antennas[j][1]]
            antinodes.append([antennas[i][0], antennas[i][1]])
            antinodes.append([antennas[j][0], antennas[j][1]])
            antinode = [antennas[i][0], antennas[i][1]]
            while not out_of_bounds:
                antinode = [antinode[0]+delta[0], antinode[1]+delta[1]]
                if antinode[0] >= 0 and antinode[0] < len(m) and antinode[1] >= 0 and antinode[1] < len(m[0]):
                    antinodes.append(antinode)
                else:
                    out_of_bounds = True

print(len(set([str(x) for x in antinodes])))