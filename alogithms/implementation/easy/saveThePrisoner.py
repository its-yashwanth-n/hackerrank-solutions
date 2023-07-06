def saveThePrisoner(n, m, s):
    # Write your code here
    value = m + s - 1
    if n >= value:
        return value
    elif value%n ==0:
        return n
    else:
        return value%n