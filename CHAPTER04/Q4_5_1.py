fun = [sum, min, max]  # sum,min,max関数を変数に代入する。
numbers = range(1, 11)  # １から１０までの範囲を変数に代入する。
for func in fun:  # 変数funcにfun変数の値を入れる。
    print("fun: {}, Result: {}".format(func.__name__, func(numbers)))
    # formatを使って、funcにnumbers変数を引数として渡してループ処理をする。
