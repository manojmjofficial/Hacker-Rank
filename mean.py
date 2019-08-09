#Program to print mean, median and mode
import statistics
n=int(input())
a=[]
for i in range(0,n):
    arr=int(input())
    a.append(arr)
print(statistics.mean(a))
print(statistics.median(a))
print(statistics.mode(a))
