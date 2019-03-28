def non_blank_lines(thing):
    """thing에서 비어있지 않은 줄 수를 반환한다.""" 
    
    count = 0
    for line in thing:
        if line.strip():
            count += 1
    return count
