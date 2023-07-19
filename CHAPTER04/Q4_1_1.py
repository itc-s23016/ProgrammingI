def f(n):
    a, b = 0, 1  # a,bに０と１を入れる。
    while a < n:  # aがnより小さかったら
        print(a, end=" ")  # aをprintする。
        a, b = b, a + b  # aにbの値を入れて、bにaとbを足した値を入れる。


print(f(1000))
