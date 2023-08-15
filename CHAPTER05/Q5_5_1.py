# xに'abcabcabc'の文字列が入り、もしｘに'ab'が含まれていなかった場合。
a = {x for x in "abcabcabc" if x not in "ab"}
print(a)
