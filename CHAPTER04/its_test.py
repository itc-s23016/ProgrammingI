s = input()
a = [int(input()) for i in range(int(s))]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i] ^= a[j]
            a[j] ^= a[i]
            a[i] ^= a[j]
a.reverse()
print(*a)
