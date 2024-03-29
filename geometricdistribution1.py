#Program to find Geometric Distribution
def geometric(p, n, x):
    return p**x * (1-p)**(n-x)
numerator, denominator = list(map(float, input().strip().split(" ")))
n = float(input())
p = numerator / denominator
print(round(geometric(p, n, 1), 3))
