def Nhap():
    n=int(input('SoLuong:'))
    m = input('DonVi(Muong cafe, Muong Canh, Coc):')
    return n,m
def doidonvi(m,n):   
    cafe=0
    canh=0
    coc=0
    if m.lower()=='muong cafe':
        cafe=n
    elif m.lower()=='muong canh':
        cafe=n*3
    elif m.lower()=='coc':
        cafe=n*48
    coc=cafe//48
    cafe=cafe%48
    canh=cafe//3
    cafe=cafe%3
    print(f'{coc} coc, {canh} muong canh, {cafe} muong cafe')
n,m=Nhap()
doidonvi(m,n)  