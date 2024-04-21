# https://www.hackerrank.com/challenges/compare-the-triplets/problem

# Time Complexity: O(n)
# Space Complexity O(1)

def compareTriplets(a, b):
    score = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1

    return score
