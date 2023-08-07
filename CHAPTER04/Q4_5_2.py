s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def str_float(s_coordi):
    p = s_coordi.split(",")  # 変数ｐに与えられた文字列をカンマで区切る。
    return list(map(float, p))  # float型に変換して、数値リストを返す。


def str_float_coord(s_coordi_list):
    return map(str_float, s_coordi_list)  # str_floatを使って、リストを処理する。


f_coordi_list = list(str_float_coord(s_coordi_list))  # list関数を使って、計算の答えを出す。

print(f_coordi_list)
