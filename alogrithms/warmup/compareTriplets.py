# Problem Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def compareTriplets(a, b):

    points = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points
