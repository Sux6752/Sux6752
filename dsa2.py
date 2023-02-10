A=int(input("A- "))
B=int(input("B- "))
if A < B:
    def chisloA(A,B):
        print(A)
        if A == B:
            return(A,B)
        else:
            A=A+1
            chisloA(A,B)
    chisloA(A,B)
if B < A:
    def chisloB(A,B):
        print(A)
        if A == B:
            return(A,B)
        else:
            A=A-1
            chisloB(A,B)
    chisloB(A,B)