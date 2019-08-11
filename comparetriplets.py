#program to compare the triplets
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
c=0
d=0
for i in range(0,3):
	if a[i]>b[i]:
		c+=1
	elif a[i]<b[i]:
		d+=1
print(c," " ,end='')
print(d)
