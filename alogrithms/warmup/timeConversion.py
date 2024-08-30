# Problem Link: https://www.hackerrank.com/challenges/time-conversion/problem

# Time Complexity: O(1)
# Space Complexity: O(1)


def timeConversion(s):
    size = 10  # size of string is always constant

    start = s[0:2]
    middle = s[2: size - 2]
    end = s[-2:]

    if start == "12" and end == "AM":
        return "00" + middle
    elif start != "12" and end == "PM":
        return str(int(start) + 12) + middle
    return start + middle
