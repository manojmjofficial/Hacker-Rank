#Program to find number of pairs in an array
input()
socks = input().strip().split()
pairs = 0
for element in set(socks):
    pairs += socks.count(element) // 2
print(pairs)
