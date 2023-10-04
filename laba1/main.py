a = []
b = []

while len(a) < 3:
    f = int(input())
    a.append(f)

while len(b) < 3:
    f = int(input())
    b.append(f)

def sred(a, b):
    x = a[1]
    y = b[1]
    return [x, y]

c = sred(a, b)

print(c)