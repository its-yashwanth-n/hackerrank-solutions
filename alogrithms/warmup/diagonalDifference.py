# Problem Link: https://www.hackerrank.com/challenges/diagonal-difference/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def diagonalDifference(arr):

    size, primary_diag, secondary_diag = len(arr), 0, 0

    for i in range(size):
        primary_diag += arr[i][i]
        secondary_diag += arr[i][size - i - 1]
    return abs(primary_diag - secondary_diag)
