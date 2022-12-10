if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    scores_sorted = sorted(list(set(scores)))
    names = sorted([name for [name, score] in students if score == scores_sorted[1]])
    result = [print(name) for name in names]
