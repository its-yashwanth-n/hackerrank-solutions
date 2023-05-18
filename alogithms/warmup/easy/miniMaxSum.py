def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    overall_sum = sum(arr)
    
    max_ele = overall_sum - sorted_arr[0]
    min_ele = overall_sum - sorted_arr[len(sorted_arr)-1]

    print(min_ele, max_ele)