my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chibe", "saitama", "gunma"]
my_list2 = []
for i in my_list:  # 変数iにmy_listを入れる。
    if len(i) >= 6:  # len関数を使ってif文を作る
        my_list2.append(i)  # appennd()を使ってmy_list2に入れる。
print(my_list2)
