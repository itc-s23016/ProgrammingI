with open("numbers.py", "r") as f:  # numbers.pyを読み込む。
    sum = 0
    for data in f:  # 変数dataにnumbers.pyの中身を入れる。
        num = int(data)  # 変数numにint型に直した変数dataを入れる。
        sum += num  # 変数sumに変数numの値を入れる。
    print(sum)  # 合計を出す
