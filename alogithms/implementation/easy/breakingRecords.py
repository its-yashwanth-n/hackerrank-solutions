def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    result = [0,0] # index 0 for best and 1 for worst
    
    for i in range(1, len(scores)):
        if min_score > scores[i]:
            result[1] += 1
            min_score = scores[i]
        elif max_score < scores[i]:
            result[0] += 1
            max_score = scores[i]
    return result 