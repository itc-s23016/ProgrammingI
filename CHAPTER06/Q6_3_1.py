class Nigiri:  # Nigiriというクラスを作る。
    category = "にぎり"
    top = "ねた"
    base = "しゃり"
    prise = 100

    def show_attributes(self):
        print(
            "top: {}, base: {}, category: {}".format(self.top, self.base, self.category)
        )
        print("prise: {}".format(self.prise))


class Katsuo(Nigiri):  # Nigiriクラスを元にKatsuoクラスを作って、topを上書きして、toppingを加える。
    top = "かつお"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))


k1 = Katsuo()
k1.show_attributes()
