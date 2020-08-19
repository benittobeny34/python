def partition(arr):
    low,mid,high = 0,0,len(arr)-1

    while mid <= high:
        if arr[mid] == 'R':
            arr[mid],arr[low] = arr[low],arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
    return arr



values = ['R','B','G','R','B','R','B','G','B','R','B']

print(partition(values))
