def birthdayCakeCandles(candles):
    max = candles[0]
    count = 1
    for i in range(1, len(candles)):
        if max < candles[i]:
            max = candles[i]
            count = 1
        elif max == candles[i]:
            count += 1
    return count