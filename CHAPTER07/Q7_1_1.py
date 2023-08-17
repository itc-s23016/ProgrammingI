name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]  # keyに対応した値をdict_tbl[key]で返す。
    except:
        return "key is not found"  # dict_tblの例外をすべて'key is not found'で返す。


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))
