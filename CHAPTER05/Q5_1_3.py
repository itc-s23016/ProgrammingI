queue = []
queue.append(1)
print("queue:", queue)
queue.append(2)
print("queue:", queue)
# popを使い、indexを０で指定して、先にappendした１を取り出す。
print("pop from queue 1st value:", queue.pop(0))
print("pop from queue 2nd value:", queue.pop(0))  # popを使って残った２を取り出す。
print("queue:", queue)
