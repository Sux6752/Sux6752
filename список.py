#a=[3,5,8,2,4,9,32]
b=[]
c=[5,2,56,23,65,43,687,324]

def zn(c):
    for i in range(len(c)):
        print(i)
        if c[i] % 2 == 0:
            b.append(c[i])
    print(b)
    return b
print(zn(c))