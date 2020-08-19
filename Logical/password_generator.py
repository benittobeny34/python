import random as r
def appropriate_char(val):
    return chr(val)
def getchar():
    x=r.randrange(1,30)
    x %= 4
    c=''
    if (x==0):
        c = appropriate_char(r.randrange(35,39))
    elif x==1:
        c = appropriate_char(r.randrange(48,58))
    elif(x==2):
        c = appropriate_char(r.randrange(64,90))
    elif(x==3):
        c = appropriate_char(r.randrange(97,122))
    return c
    


def password_generator():
    password = ''
    for i in range(15):
        c = getchar()
        password += c
    return password
        

print(password_generator())


