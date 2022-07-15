n = int(input())
t = list(map(int, input().split()))
a = sorted(t)
b = []
for i in range(n):
    idx = a.index(t[i])
    b.append(idx)
    a[idx] = -1
print(*b)