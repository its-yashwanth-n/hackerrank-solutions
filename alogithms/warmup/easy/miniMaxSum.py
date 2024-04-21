# https://www.hackerrank.com/challenges/mini-max-sum/problem

# Time Complexity: O(n)
# Space Complexity O(1)

def miniMaxSum(arr):

    min_element = arr[0]
    max_element = arr[0]
    overall_sum = 0

    for i in range(len(arr)):
        overall_sum += arr[i]
        max_element = max(arr[i], max_element)
        min_element = min(arr[i], min_element)

    print((overall_sum-max_element), (overall_sum-min_element))

# Time Complexity: O(n log n)
# Space Complexity O(n)

def miniMaxSum(arr):

    sorted_arr = sorted(arr)
    overall_sum = sum(arr)

    max_ele = overall_sum - sorted_arr[0]
    min_ele = overall_sum - sorted_arr[len(sorted_arr)-1]

    print(min_ele, max_ele)
