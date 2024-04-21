def pageCount(n, p):
    total_turns = int(n/2)
    from_start = int(p/2)
    from_end = total_turns - from_start
    answer = min(from_start, from_end)
    
    return answer