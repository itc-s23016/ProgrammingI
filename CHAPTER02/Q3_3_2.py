my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in my_list:  # 変数nにmy_listを入れる。
    if n % 2 != 0:  # 変数nを２で割り、あまりが０じゃない時
        x += n  # x+1+1+3+5+13=23 x=23
print(x)
