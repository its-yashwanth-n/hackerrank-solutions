# https://www.hackerrank.com/challenges/between-two-sets/problem

# TODO: improve this to be more efficient
def getTotalX(a, b):
    initial = step = a[-1]
    end = b[0]

    count = 0

    while initial <= end:
        flag = 0

        for number in a:
            if initial % number != 0:
                flag = 1
                break

        for number in b:
            if number % initial != 0:
                flag = 1
                break

        if flag == 0:
            count += 1
        initial += step

    return count
