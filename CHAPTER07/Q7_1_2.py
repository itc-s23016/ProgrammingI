def list_average(x):
    try:
        return sum(x) / len(x)  # リストの平均を求める式
    except:
        print("list_length:", len(x))  # リストの中が０だった場合、Noneを返す。
        return None


print(list_average([3.9, 4.5, 2, 3]))
print(list_average([]))
