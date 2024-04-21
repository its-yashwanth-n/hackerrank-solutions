def birthday(s, d, m):

    result = 0
    size = len(s)

    for i in range(size-m+1):

        count = 1
        sum_val = s[i]

        while count < m:
            sum_val += s[i+count]
            count += 1
        if sum_val == d:
            result += 1
            
    return result