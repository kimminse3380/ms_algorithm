n, k = input().split()
n = int(n)
k = int(k)
 
 
def check(n, k):
    if n < k * (k + 1) // 2:
        return -1
    else:
        left = n - k * (k + 1) // 2
        if left % k == 0:
            return k - 1
        else:
            return k
 
 
print(check(n, k))
