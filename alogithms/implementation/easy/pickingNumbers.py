def pickingNumbers(a):
    a.sort()
    size = len(a)
    result = 0
    index = 0
    
    while index < size:
        current_ele = a[index]
        count = 0
        for j in range(index,size):
            if a[j] - current_ele <= 1:
                count = count + 1
                index += 1
            else:
                index = j
                break;
        result = max(result, count)

    return result