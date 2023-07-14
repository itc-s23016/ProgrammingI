import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num4 = "".join(random.sample(numbers, k=4))  # ランダムで数字を４桁取り出す。
while True:
    con = input()
    if con == num4:  # input()から読み取った数字が変数num4と同じであれば
        break  # コードを終了する。
    if len(con) != 4:  # input()の数字が４桁じゃなかったら
        print("input 4 numbers.")  # ４桁を入力してください。と出力する。
        continue  # 下のコードを一回行わない。
    ans = ""
    for i in range(4):  # 変数iにrange()で範囲を決める。
        if num4[i] == con[i]:  # 変数num4とinput()の値が同じであれば
            ans += con[i]  # 変数ansにinput()の値を入れる。
        else:  # それ以外は
            ans += "X"  # 変数ansにｘを入れる。
    print("-> " + ans)
