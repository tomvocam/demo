def Nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    d=b**2-4*a*c
    if d<0:
        print('Phuong trinh vo nghiem')       
    elif d==0:
        print('Phuong trinh co nghiem kep')
        x1=x2=-(b/2*a)
        print(f'x1=x2={x1}')
        return x1,x2
    elif d>0:
        print('Phuong trinh co hai nghiem')
        x1=(-b+d**0.5)/2/a
        x2=(-b-d**0.5)/2/a
        inkq(x1,x2)
        return x1,x2
def inkq(x1,x2):
    print(f'x1={x1}')
    print(f'x2={x2}')    
a,b,c=Nhap()
giaipt(a,b,c)
