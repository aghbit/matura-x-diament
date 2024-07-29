def sol(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return -1
    
n = int(input())
print(sol(n))
