i = """3   4
4   3
2   5
1   3
3   9
3   3"""

arr = [x.split("   ") for x in i.split("\n")]
arr1, arr2 = sorted([int(x[0]) for x in arr]), sorted([int(x[1]) for x in arr])
print(sum([abs(x - y) for x, y in zip(arr1, arr2)]))