#to find the difference between the sum of the diagonals of a matrix
def diagonalDifference(arr):
    one=0
    two=0
    for i in range(0,n):
        for j in range(0,n):
            if (i == j):
                one+=arr[i][j]
    for i in range(0,n):
        for j in range(0,n):
            if (i == n - j - 1):
                two+=arr[i][j]
    if one>two:
        return (one-two)
    else:
        return (two-one)

n = int(input().strip())
arr = []
for _ in range(n):
	arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)
