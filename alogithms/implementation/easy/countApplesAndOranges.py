def countApplesAndOranges(s, t, a, b, apples, oranges):
    # to use biggest if 2 in range instead of 2 loops
    n_apples = len(apples)
    n_oranges = len(oranges)
    
    max_count = max(n_apples, n_oranges)
    result = [0, 0]
    
    for i in range(max_count):
        if n_apples > 0:
            a_distance = a + apples[i]
            if a_distance >= s and a_distance <= t:
                result[0] += 1
        if n_oranges > 0:
            b_distance = b + oranges[i]   
            if b_distance >= s and b_distance <= t:
                result[1] += 1
        n_apples -= 1
        n_oranges -= 1
        
    print(result[0])
    print(result[1])  