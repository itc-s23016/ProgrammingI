mountain_in_japan = {"juji": 3776, "kitadake": 3193, "okuhodakadake": 3190, "dummy": 0}
mountain_in_japan_sorted = sorted(
    # mountain_in_japanの要素をitems()でkeyと値を出力し、keyの標高をラムダ式で指定して降順にするためにreverse=Trueを指定する。
    mountain_in_japan.items(),
    key=lambda x: x[1],
    reverse=True,
)
print(mountain_in_japan_sorted)
