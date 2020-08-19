def func(d):
    return d[1]
data = [
    ['two',2],
    ['one',1],
    ['four',4],
    ['three',3]
    ]
data.sort(key = lambda d:d[1])
print(data)

values = [1,2,3,8,3,5,9,10,45,20,34,33]
values.sort(reverse=True)
print(values)
