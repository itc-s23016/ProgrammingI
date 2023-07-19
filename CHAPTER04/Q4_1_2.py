def f(n):
    a, b = 0, 1  # aとbに０と１を入れる。
    result = []  # 空のリストを用意する。
    while a < n:  # aがnより小さかったら
        result.append(a)  # aの値を空のリストに入れる。
        a, b = b, a + b  # aにbの値を入れ、bにaとbの値を足した値を入れる。
    print(result)


f(1000)
