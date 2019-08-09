#calculate the fractions of its elements that are positive, negative, and are zeros
d=0
b=0
c=0
n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)
for i in range(0,n):
	if a[i]>0:
		d+=1
	elif a[i]<0:
		b+=1
	else:
		c+=1
print("%.6f" %(d/n))
print("%.6f" %(b/n))
print("%.6f" %(c/n))
	
