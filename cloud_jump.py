# Program to find number of jumps to win
n = int(input())
c = list(map(int,input().strip().split()))
count = 0
i = 0 
while (i < n-2):
      i += (c[i+2] == 0) + 1
      count += 1
print (count+(i==n-2))
