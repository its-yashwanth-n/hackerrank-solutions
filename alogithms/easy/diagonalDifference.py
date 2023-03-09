def diagonalDifference(arr):
    primary_diag = 0
    second_diag = 0
    size = len(arr)
    for i in range(size):
        primary_diag += arr[i][i]
        second_diag += arr[i][size-i-1]
    return abs(primary_diag - second_diag)