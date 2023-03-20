def Nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
def inkq(n,t):
    print(f'{n}!={t}')
n=Nhap()
t=giaithua(n)
inkq(n,t)

















