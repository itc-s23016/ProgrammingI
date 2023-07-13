import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers2 = random.sample(numbers, k=4)
numbers3 = "".join(numbers2)
while True:
    val = input()
    if val == numbers3:
        print("Correct")
        break
    else:
        print(val, ": NotCorrect")
