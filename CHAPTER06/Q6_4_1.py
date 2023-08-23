f = open("some.py")  # some.pyファイルを開く。
c = 0
for a in f:
    print(a, end="")
    if c == 2:  # cの値が２になったら、breakで止める。
        break
    c += 1
f.close()  # some.pyファイルを閉じる。
