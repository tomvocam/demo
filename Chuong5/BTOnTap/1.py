def Nhap():
    L=input('L=').split()
    L=[int(x) for x in L] #Chuyển thành dạng int
    x=int(input('x='))
    k=int(input('k='))
    return L,x,k
def add(L, x, k):
    if k > len(L):
        L.append(x)
    else:
        L.insert(k, x)
    return L
def inkq(L):
    print(L)
L,x,k=Nhap()
add(L,x,k)
inkq(L)
