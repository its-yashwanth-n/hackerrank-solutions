def getTotalX(a, b):
    # Write your code here
    first = b[0]
    last = a[-1]
    result = 0
    
    while last <= first:
        flag = 0
        for i in range(len(a)):
            if last % a[i] != 0:
                flag = 1
                break
        for j in range(len(b)):
            if b[j] % last != 0:
                flag = 1
                break
        if flag == 0:
            result += 1
        last += 1
    return result