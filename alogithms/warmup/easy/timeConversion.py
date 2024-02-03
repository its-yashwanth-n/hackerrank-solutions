# Time Complexity: O(1)
# Space Complexity O(1)

def timeConversion(s):
    # size of string is always constant
    size = 10

    start = s[0:2]
    middle = s[2:size-2]
    end = s[size-2:size]

    if start == "12" and end == "AM":
        start = "00"
    elif end == "PM" and start != "12":
        start = str(int(start)+12)

    return start + middle
