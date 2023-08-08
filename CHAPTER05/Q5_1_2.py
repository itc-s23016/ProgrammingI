stack = []
stack.append(1)  # appendを使って、１を追加する。
print("stack:", stack)
stack.append(2)  # appendを使って、２を追加する。
print("stack:", stack)
print("pop 1st value:", stack.pop())  # popを使って、スタックの先頭の２を取り出す。
print("pop 2nd value:", stack.pop())  # popを使って、残っている１を取り出す。
print("stack:", stack)
