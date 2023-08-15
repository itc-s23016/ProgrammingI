A = {x for x in range(21)}  # ２１までの範囲までの要素を持つｘ
B = {y for y in range(21) if y % 2 == 0}  # ２１までの範囲で、偶数の要素を持つｙ
C = A - B
print(C)
