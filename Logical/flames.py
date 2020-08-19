def flames(name1,name2):
    flame = ['f','l','a','m','e','s']
    name1 = [x for x in name1 if x != ' ']
    name2 = [x for x in name2 if x != ' ']
    less,high = [name1,name2] if len(name1)<len(name2) else [name2,name1]
    for i in range(len(less)):
        for j in range(len(high)):
            if less[i] == high[j]:
                less[i] = high[j] = '*'
    count = 0
    count = sum(1 for x in high if x!='*')
    count = count + sum(1 for x in less if x!='*' )
    offset = 0
    while len(flame)>1:
        remainder = (offset + count) % len(flame)
        del flame[remainder-1]
        offset = remainder-1 if remainder > 0 else 0
        
    return flame[-1]
    
        
        


    
            



name1 = input('enter your name').strip()
name2 = input('enter your partner name').strip()
print(flames(name1,name2))
