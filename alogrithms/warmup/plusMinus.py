# Problem Link: https://www.hackerrank.com/challenges/plus-minus/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def plusMinus(arr):
    array_size = len(arr)
    positive, negative, zero = 0, 0, 0

    for val in arr:
        if val == 0:
            zero += 1
        elif val > 0:
            positive += 1
        else:
            negative += 1

    print(positive / array_size)
    print(negative / array_size)
    print(zero / array_size)
