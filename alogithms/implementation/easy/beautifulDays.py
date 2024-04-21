def reverse_number(number):
    reverse = 0

    while number > 0:
        remainder = number % 10
        reverse = (reverse*10) + remainder
        number = number//10

    return reverse


def beautifulDays(i, j, k):
    days = 0

    while i <= j:
        reverse = reverse_number(i)
        if (abs(i-reverse) % k) == 0:
            days += 1
        i += 1

    return days
