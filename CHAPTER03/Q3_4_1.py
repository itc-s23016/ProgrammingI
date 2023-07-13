for i in range(10):  # 変数iに０〜９までの範囲の数値を入れる。
    if i % 2 == 0:  # 変数iを２で割って、あまりが０だった時
        continue  # printしない
    print(i)
