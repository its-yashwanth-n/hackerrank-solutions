def viralAdvertising(n):
    people = 5
    no_of_recipients = 3
    new_advertisers = 0

    for i in range(n):
        new_advertisers += people // 2
        people = (people // 2) * no_of_recipients
        
    return new_advertisers