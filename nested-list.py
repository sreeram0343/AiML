
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [student[1] for student in students]

    second_lowest = sorted(set(scores))[1]

    names = [student[0] for student in students if student[1] == second_lowest]

    for name in sorted(names):
        print(name)