def Nhap():
    L=input('L=').split()
    L=[int(x) for x in L]
    x=int(input('x='))
def delete(L,x):
    while x in L:
        L.remove(x)
def inkq(L):
    print(L)
