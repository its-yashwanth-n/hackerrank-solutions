# Time Complexity: O(n^2)
# Space Complexity O(1)

def staircase(size):

    for i in range(1, size+1):
        space = size-i
        print(" " * space + "#"*i)
