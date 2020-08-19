def value(char):
    return ord(char)

def simple_hash(prev,start,new):
    return prev-value(start)+value(new)


def find_matches(pattern,string):
    matches = []
    k = len(pattern)
    
    pattern_value=0
    for i,char in enumerate(pattern):
        pattern_value += value(char)

    hash_value =0
    for i,char in enumerate(string[:k]):
        hash_value += value(char)
        
    if pattern_value == hash_value:
        if pattern == string[:k]:
            matches.append(0)

    

    for i in range(len(string)-k):
        hash_val = simple_hash(hash_value,string[i],string[i+k])
        if hash_value == pattern_value:
            if pattern == string[i+1 : i+k+1]:
                matches.append(i + 1)
    return matches

if __name__ == '__main__':
    string = input('enter the string:')
    pattern = input('enter the pattern to match the string:')
    print(find_matches(pattern,string))
    
        
        
                 
