# Problem Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# Time Complexity: O(n)
# Space Complexity: O(1)


def birthdayCakeCandles(candles):

    max_val = candles[0]
    count = 1

    for val in candles[1:]:
        if max_val < val:
            max_val = val
            count = 1
        elif max_val == val:
            count += 1

    return count
