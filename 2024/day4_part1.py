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
for i in range(0, len(s)):
    for j in range(0, len(s[i])-3):
        horizontal = s[i][j:j+4]
        if horizontal == "XMAS" or horizontal == "SAMX":
            occurences += 1
for i in range(0, len(s[0])):
    for j in range(0, len(s)-3):
        vertical = s[j][i]+s[j+1][i]+s[j+2][i]+s[j+3][i]
        if vertical == "XMAS" or vertical == "SAMX":
             occurences += 1
for i in range(0, len(s)-3):
    for j in range(0, len(s[0])-3):
        diagonal = s[i+0][j+0]+s[i+1][j+1]+s[i+2][j+2]+s[i+3][j+3]
        if diagonal == "XMAS" or diagonal == "SAMX":
             occurences += 1
for i in range(0, len(s)-3):
    for j in range(3, len(s[0])):
        diagonal = s[i+0][j+0]+s[i+1][j-1]+s[i+2][j-2]+s[i+3][j-3]
        if diagonal == "XMAS" or diagonal == "SAMX":
             occurences += 1
print(occurences)