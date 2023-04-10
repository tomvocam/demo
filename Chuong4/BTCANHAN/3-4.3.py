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
        return None     
    elif d==0:
        # print('Phuong trinh co nghiem kep')
        x1=x2=-(b/2*a)
        # print(f'x1=x2={x1}')
        
    elif d>0:
        # print('Phuong trinh co hai nghiem')
        x1=(-b+d**0.5)/2/a
        x2=(-b-d**0.5)/2/a
        # inkq(x1,x2)
    return x1,x2
def inkq(x1,x2):
    if x1==x2:
        print('Phuong trinh co nghiem kep')
        print(f'x1=x2={x1}')
    elif x1!=x2:
        print('Phuong trinh co hai nghiem')
        print(f'x1={x1}')
        print(f'x2={x2}')    
a,b,c=Nhap()
ff=giaipt(a,b,c)
if ff!=None:
    x1,x2=giaipt(a,b,c)
    inkq(x1,x2)
