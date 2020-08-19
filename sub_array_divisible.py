def solution(arr):
    count = 0
    prefix_products = []
    i=0
    j=len(arr)-1;
    total = sum(arr[i:j])
    for index in range(len(arr)//2):
        
        i += 1
        total = sum(arr[i:j+1])
        if prefix_products:
            prefix_products.append([i-1])
        else:
            prefix_products.append(prefix_products[-1]*arr[i])
        j -= 1
        i -= 1
        total = sum(arr[i:j+1])
        i +=1
        total = sum(arr[i:j+1])
        if suffix_products:
            suffix_products.append(arr[j+1])
        else:
            suffix_products.append(suffix_products[-1]*arr[i])
        
        







li = [1,2,3,4,5,6,7]
solution(li)
