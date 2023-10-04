n = int(input())
a = []

while len(a) < n:
    f = int(input())
    a.append(f)

def summa(x):
    return sum(x)

print(summa(a))