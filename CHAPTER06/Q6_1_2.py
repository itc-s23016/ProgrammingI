class Person:  # PersonというClassを作る。
    def __init__(self, name="", nationality="", birth="", address=""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):  # show_attributes()というメソッドにself.属性を使う。
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいる所:", self.address)


heroine = Person("かぐや姫", "日本", "６８５", "静岡県富士市")
heroine.show_attributes()
hero = Person("金太郎", "日本", "９５６", "静岡県駿東郡小山町")
hero.show_attributes()
