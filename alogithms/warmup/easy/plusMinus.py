# https://www.hackerrank.com/challenges/plus-minus/problem

# Time Complexity: O(n)
# Space Complexity O(1)

def plusMinus(arr):
    size = len(arr)

    # creating variables indices for readability
    positive = 0
    negative = 1
    zeros = 2

    number_count = [0, 0, 0]

    for number in arr:
        if number > 0:
            number_count[positive] += 1
        elif number < 0:
            number_count[negative] += 1
        else:
            number_count[zeros] += 1

    print(number_count[positive]/size)
    print(number_count[negative]/size)
    print(number_count[zeros]/size)
