numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:  # 変数nにnumbersのリストを入れる。
    if n > 10:  # 変数nが１０よりも大きかった時
        break  # xの値を増やさない
    x += n  # x+1+1+2+3+5+8=20 X=20
print(x)
