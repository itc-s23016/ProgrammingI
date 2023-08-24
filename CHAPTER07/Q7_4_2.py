def test_fuction():
    try:
        print("try")
        return  # try節の中でreturn文を実行すると、else節は実行されない。
    except:
        print("except")
    finally:
        print("finally")


test_fuction()
