list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if文で、list1から偶数だった場合はその値を返し、それ以外はNoneを返す。
print([x if x % 2 == 0 else None for x in list1])
