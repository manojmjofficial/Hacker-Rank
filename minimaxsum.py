#to find the minimum and maximum values that can be calculated by summing exactly four of the five integers
arr = list(map(int, input().rstrip().split()))
a=[]
for i in range(0,len(arr)):
	b=sum(arr) - arr[i]
	a.append(b)
print(min(a),end=''+' ')
print(max(a))
