# rangeで範囲を決めて、formatを使って、ゼロ埋めを４桁で行う。
str_num_list = map(lambda x: "{:04}".format(x), range(1, 8))
print(list(str_num_list))
