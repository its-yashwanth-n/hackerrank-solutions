def angryProfessor(k, a):
    count = 0

    for i in range(len(a)):
        if a[i] <= 0:
            count = count + 1
    result = "YES" if count < k else "NO"
    
    return result