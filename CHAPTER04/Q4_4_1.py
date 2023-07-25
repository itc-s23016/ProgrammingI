vote_num = 0


def vote():  # vote()という変数を作る。
    print("投票します")
    global vote_num  # global文を使って、vote_numの値を操作する。
    vote_num += 1  # vote_numの値を１増やす。


def reset_box():  # reset_box()という変数を作る。
    global vote_num  # global文を使って、vote_numの値を操作する。
    print("箱を空にします")
    vote_num = 0  # vote_numの値を０にする。


def check_box():  # check_box()という変数を作る。
    global vote_num  # global文を使って、vote_numの値を操作する。
    print("票の数は{}です".format(vote_num))  # formatを使って、vote_numの値を入れる。


vote()
check_box()
vote()
check_box()
vote()
vote()
vote()
check_box()
reset_box()
check_box()
