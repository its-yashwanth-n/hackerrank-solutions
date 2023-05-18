def utopianTree(n):

    count = 0
    height = 1
    while count < n:
        count = count + 1
        height = (height+1) if count%2==0 else (height*2)
    return height