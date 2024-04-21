def bonAppetit(bill, k, charged):
    overall_bill = sum(bill)
    actual = int((overall_bill - bill[k])/2)
    
    if charged == actual:
        print("Bon Appetit")
    else:
        print(charged - actual)