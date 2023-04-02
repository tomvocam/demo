def Nhap():
    n=int(input('Thang:'))
    y=int(input('Nam:'))
    return n,y
def inkq(n):
    if 1<=n<=7:
        if n%2==0 and n!=2:
            print(f'Thang {n} co 30 ngay.')
        elif n%2!=0:
            print(f'Thang {n} co 31 ngay')
        elif n==2 and y%4==0:
            print('Thang 2 co 29 ngay.')
        elif n==2 and y%4!=0:
            print('Thang 2 co 28 ngay.')
    if 8<=n<=12:
        if n%2==0:
            print(f'Thang {n} co 31 ngay.')
        elif n%2!=0:
            print(f'Thang {n} co 30 ngay.')
n,y=Nhap()
inkq(n)