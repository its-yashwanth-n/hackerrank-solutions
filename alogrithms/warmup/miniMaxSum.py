# Problem Link: https://www.hackerrank.com/challenges/mini-max-sum/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def miniMaxSum(arr):
    overall = 0
    min_ele = arr[0]
    max_ele = arr[0]

    for val in arr:
        overall += val
        min_ele = min(min_ele, val)
        max_ele = max(max_ele, val)

    print((overall - max_ele), (overall - min_ele))
