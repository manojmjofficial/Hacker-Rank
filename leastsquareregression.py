#Program for Least Square Regression Line
from statistics import mean, pstdev
def pearson(x, y):
    mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (len(x) * sx * sy)
def linear_regression(x, y):
    b = pearson(x, y) * pstdev(y) / pstdev(x)
    return mean(y) - b * mean(x), b
x, y = zip(*(map(float, input().split()) for _ in range(5)))
a, b = linear_regression(x, y)
print(f'{a+b*80:.3f}')
