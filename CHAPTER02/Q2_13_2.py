import random
from random import randint

print(random.randint(0, 10))
print(randint(0, 10))
# 4行目のprint文ではrandom.randint()として読み込まれている。
# 5行目のprint文ではrandint()として読み込まれている。
