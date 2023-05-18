def migratoryBirds(arr):
    size = len(arr)
    count = [0] * size
    # to count the occurrences of birds
    for i in range(size):
        count[arr[i]] += 1
    
    result = 0
    max_ele = count[0]
    # to find the bird with max count
    for i in range(1, size):
        if max_ele < count[i]:
            result = i
            max_ele = count[i]

    return result