def staircase(n):
    size = int(n)
    
    for i in range(1, size+1):
        space = size-i
        print(" " * space + "#"*i)
