n = int(input())
a = []

while len(a) < n:
    f = int(input())
    a.append(f)


def chetn(a):
    c = []
    for x in a:
        if x % 2 == 0:
            c.append(x)
    yield c


print(*chetn(a))