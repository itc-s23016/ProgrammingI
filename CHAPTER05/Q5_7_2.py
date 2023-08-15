data = [
    ["0001", "Male", "Yamada", "Tarou", "25", "Tokyo"],
    ["0002", "Male", "Satou", "Takeshi", "27", "Kanagawa"],
    ["0003", "Female", "Tanaka", "Yuko", "25", "Saitama"],
    ["0004", "Male", "Suzuki", "Ichrou", "35", "Hokkaido"],
]
member_information = {}
for record in data:  # 変数recordにdataの要素を入れる。
    key = record[0]  # リスト「０」に入っている要素を代入する。
    info = record[1:]  # リスト「１」以降に入っている要素を代入する。
    member_information[key] = info  # keyを指定して、そのkeyに対応する情報を値として代入する。
print("number", "information", sep="\t")
for key, info in member_information.items():
    print(key, info)
