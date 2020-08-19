def sorting(values):
    i,j=0,len(values)-1
    while i<=j:
        if values[i] & 1 == 1:
            i += 1
        else:
            values[i],values[j] = values[j],values[i]
            j -= 1

    print(i)
    
    for m in range(i):
        for k in range(i-1):
            if values[k] > values[k+1]:
                values[k],values[k+1] = values[k+1],values[k]
    for m in range(i,len(values)):
        for k in range(i,len(values)-1):
            if values[k] > values[k+1]:
                values[k],values[k+1] = values[k+1],values[k]        
    

    return values



lst = [0,4,5,3,7,2,1]
print(sorting(lst))
