
def palindromIsPossible(s):
    d = {}
    odd_occurance = 0
    for char in s:
        if char not in d:
            d[char]=0
        d[char] += 1
    for key,value in d.items():
        if value % 2 == 1:
            odd_occurance += 1
        if odd_occurance > 1:
            return False
    return True
        
        
            
    

s = input('enter the string')
print(palindromIsPossible(s))
