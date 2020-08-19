def countTriplets(arr, r):
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                #print(i,j,k)
                if arr[i]*r == arr[j]:
                    if arr[j]*r == arr[k]:
                        count += 1
    return count

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans))
