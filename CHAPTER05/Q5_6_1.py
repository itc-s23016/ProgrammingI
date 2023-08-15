# ｘとｙに'abcabcabc'を入れ、ｘは'ab'が含まれてない場合、ｙは'bc'が含まれてない場合。
a = {x for x in "abcabcabc" if x not in "ab"}
b = {y for y in "abcabcabc" if y not in "bc"}
print(a | b)
