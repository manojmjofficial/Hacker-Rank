#Program to find count of largest element in an array
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(ar.count(max(ar)))
