
# Complete the twoStrings function below.
def twoStrings(s1, s2):

    for i in range(len(s2)):
        print(s2[i])
        if s2[i] in s1:
            return "YES"
    return "NO"
        

t = int(input())
for q in range(t):
    s1 = input()
    s2 = input()
    result = twoStrings(s1,s2)
    print(result)
