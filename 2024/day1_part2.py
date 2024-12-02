i = """3   4
4   3
2   5
1   3
3   9
3   3"""

arr = [x.split("   ") for x in i.split("\n")]
arr1, arr2 = [int(x[0]) for x in arr], [int(x[1]) for x in arr]
similarity_score = sum([y * sum([1 if x == y else 0 for x in arr2]) for y in arr1])
print(similarity_score)