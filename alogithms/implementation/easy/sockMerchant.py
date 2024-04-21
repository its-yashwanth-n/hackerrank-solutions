def sockMerchant(n, ar):
    sock_dict = {}
    pairs = 0
    
    for i in range(n):
        if ar[i] in sock_dict:
            sock_dict[ar[i]] += 1
            if (sock_dict[ar[i]]%2 == 0):
                pairs += 1
                sock_dict[ar[i]] -= 2
        else:
            sock_dict[ar[i]] = 1
            
    return pairs