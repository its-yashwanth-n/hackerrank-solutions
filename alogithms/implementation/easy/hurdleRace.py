def hurdleRace(k, height):
    maxHeight = max(height)
    result = 0 if maxHeight <= k else (maxHeight-k)
    
    return result