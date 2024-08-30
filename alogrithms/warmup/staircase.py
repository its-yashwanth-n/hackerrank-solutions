# Problem Link: https://www.hackerrank.com/challenges/staircase/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def staircase(n):
    for i in range(1, n + 1):
        print((n - i) * " " + (i) * "#")
