def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
    return score