def Nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    kq=a
    if kq<b:
        kq=b
    if kq<c:
        kq=c
    return kq
def inkq(kq):
    print('So lon nhat la:',kq)
a,b,c=Nhap()
kq=max3(a,b,c)
inkq(kq)