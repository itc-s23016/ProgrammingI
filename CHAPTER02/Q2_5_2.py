a = "○ "
b = "●h"
answer = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer += a
        else:
            answer += b
    answer += "\n"
print(answer)
