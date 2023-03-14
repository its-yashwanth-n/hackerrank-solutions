def countingValleys(steps, path):

    valley_count = 0
    level = 0 
    
    for i in range(steps):
        if path[i] == "U":
            level += 1
        elif path[i] == "D":
            level -= 1
        if path[i] == "U" and level == 0:
            valley_count += 1
    return valley_count