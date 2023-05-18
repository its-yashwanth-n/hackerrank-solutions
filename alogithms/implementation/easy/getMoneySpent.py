def getMoneySpent(keyboards, drives, b):
    result = -1

    for kbd in keyboards:
        for usb in drives:
            value = kbd + usb
            result = max(result, value) if value <= b else result
    
    return result