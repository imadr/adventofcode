s = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


occurences = 0
s = s.split("\n")
for i in range(1, len(s)-1):
    for j in range(1, len(s[i])-1):
        if s[i][j] == "A":
            diagonal_1 = s[i-1][j-1]+"A"+s[i+1][j+1]
            diagonal_2 = s[i-1][j+1]+"A"+s[i+1][j-1]
            if (diagonal_1 == "MAS" or diagonal_1 == "SAM") and (diagonal_2 == "MAS" or diagonal_2 == "SAM"):
                occurences += 1

print(occurences)