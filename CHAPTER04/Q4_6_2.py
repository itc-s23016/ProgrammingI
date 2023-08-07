import random


def generate_students_data(num_students=10):
    students_data = []  # 空のリストを用意する。
    for i in range(num_students):  # iにnum_studentsの値を入れる。
        name = "n" + str(random.randint(10, 50))  # 名前と
        height = random.randint(150, 190)  # 身長と
        weight = random.randint(50, 80)  # 体重をランダムで取得。
        students_data.append((name, height, weight))  # その値をappendする。
        if i == 0:
            print("i, name, height, weight")
        if i < 2 or i == num_students - 1:
            print(i, name, height, weight)
        elif i == 2:
            print("...")
    return students_data


students_data = generate_students_data(10)
# sortedを使って、身長が低い順で並び替える。
students_by_height = sorted(students_data, key=lambda s: s[1])
# sortedを使って、体重が低い順で並び替える。
students_by_weight = sorted(students_data, key=lambda s: s[2])
print("\nSort by height")
for student in students_by_height:
    print(student)
print("\nSort by weight")
for students in students_by_weight:
    print(students)
