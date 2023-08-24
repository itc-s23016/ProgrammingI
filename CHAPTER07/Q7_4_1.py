fname = "out_test.txt"
s = "Hello out_test.txt"
with open(fname, "w") as f:  # 書き込みモードで'Hello out_test.txt'と書き込む。
    f.write(s)

with open(fname, "r") as f:  # 読み込みモードで'out_test.txt'を読み込む。
    for line in f:
        print(line, end="")
