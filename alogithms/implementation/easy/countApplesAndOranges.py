# https://www.hackerrank.com/challenges/apple-and-orange/problem

# Time Complexity: O(n + m)  where m is size of list - apples, and n is size of list - oranges
# Space Complexity O(1)

def countApplesAndOranges(s, t, a, b, apples, oranges):
    result = [0, 0]

    for apple in apples:
        a_distance = a + apple
        if a_distance >= s and a_distance <= t:
            result[0] += 1
    for orange in oranges:
        b_distance = b + orange
        if b_distance >= s and b_distance <= t:
            result[1] += 1

    print(result[0])
    print(result[1])
