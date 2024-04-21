# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

# Time Complexity: O(n)
# Space Complexity O(1)

def birthdayCakeCandles(candles):
    max_height = candles[0]
    count = 1

    for i in range(1, len(candles)):
        if max_height < candles[i]:
            max_height = candles[i]
            count = 1
        elif max_height == candles[i]:
            count += 1

    return count


# Simpler method
def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count
