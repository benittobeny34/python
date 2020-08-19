'''def autocomplete:
    results = []
    for word in words:
        if word.startswith(s):
            results.add(word)
    return results

#the above function runs o(n) time complexity we can reduce this using tries.
'''


ENDS_HERE = '#'

class Trie:
    def __init__(self):
        self.trie = {} #dictionary
    def insert(self,text):
        trie = self.trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE]=True
    def find(self,prefix_to_find):
        trie = self.trie
        for char in prefix_to_find:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return self._elements(trie)
    def _elements(self,d):
        result = []
        for c,v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [ c + s for s in self._elements(v)]
            result.extend(subresult)
        return result
    
    def autocomplete(self,prefix):    
        suffixes = trie.find(prefix)
        return [prefix + w for w in suffixes]


words = ['beni','ball','bat','football','soccer','foot','feet','foo','font','benitto','bell']
trie = Trie()
for word in words:
    trie.insert(word)
print('successfully inserted')

print(trie.autocomplete('ba'))
print(trie.autocomplete('fo'))
print(trie.autocomplete('be'))


    
        

    
    
