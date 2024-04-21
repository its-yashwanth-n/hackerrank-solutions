# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# Time Complexity: O(n)
# Space Complexity O(1)

def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    result = [0, 0]  # index 0 for best and 1 for worst

    for val in scores:
        if min_score > val:
            result[1] += 1
            min_score = val
        elif max_score < val:
            result[0] += 1
            max_score = val
    return result
