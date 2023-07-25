vote_num = 0


def vote(vote_n):  # vote変数とvoteの値を作る。
    print("投票します")
    vote_n += 1  # vote_nの値を１増やす。
    return vote_n


def reset_box(vote_n):  # reset_box変数とvoteの値を作る。
    print("票を空にします")
    vote_n = 0  # vote_nの値を０にする。
    return vote_n


def check_box(vote_n):  # check_box変数とvoteの値を作る。
    print("票の数は{}です".format(vote_n))  # formatを使って、vote_nの値を入れる。
    return


vote_num = vote(vote_num)
check_box(vote_num)
vote_num = vote(vote_num)
check_box(vote_num)
for i in range(3):
    vote_num = vote(vote_num)
check_box(vote_num)
vote_num = reset_box(vote_num)
check_box(vote_num)
