n=int(input())
def chislo(n):
    print(n)
    if n == 1:
        return 1
    else:
        n=n-1
        chislo(n)
chislo(n)
