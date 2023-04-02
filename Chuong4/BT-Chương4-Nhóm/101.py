def Nhap():
    a=int(input('Tu so:'))
    b=int(input('mau so:'))
    return a,b
def toigian(a,b):
    for i in range(1,a+1):
        if b%i==0:
            b/=a
            B=int(b)
            a/=a
            A=int(a)
            print(f'Phan so toi gian la:{A}/{B}')
    return a,b
a,b=Nhap()
toigian(a,b)