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
        return trie


words = ['beni','ball','bat','football','soccer']
trie = Trie()
for word in words:
    trie.insert(word)
print('successfully inserted')
for key,value in trie.trie.items():
    print(key,'=>',value)
    
        

    
    
