def plusMinus(arr):
    size = len(arr)
    positive = 0
    negative = 1
    zeros = 2
    number_count = [0,0,0]

    for i in range(size):
        if arr[i] > 0:
            number_count[positive] += 1
        elif arr[i] < 0:
            number_count[negative] += 1
        else:
            number_count[zeros] += 1
            
    print(number_count[positive]/size) 
    print(number_count[negative]/size)
    print(number_count[zeros]/size)