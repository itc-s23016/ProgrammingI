def f(*arf):
    result = []  # 空のリスト
    for n in arf:  # nにarfの値を入れる。
        result.append(n * n)  # resultにｎを二乗した値を入れる。
    print(result)


num = list(range(100))  # numに１００までの範囲の数値をリストに入れる。
f(*num)
