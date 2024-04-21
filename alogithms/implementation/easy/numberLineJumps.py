# https://www.hackerrank.com/challenges/kangaroo/problem

# Time Complexity: O(1)
# Space Complexity O(1)

def kangaroo(x1, v1, x2, v2):

    if (v2 >= v1):
        # this is valid due x2 > x1 constraint
        return "NO"
    if ((x1-x2) % (v1-v2) == 0):
        return "YES"
    else:
        return "NO"
