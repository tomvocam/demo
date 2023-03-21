def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def SoHopLe(x):
    if x <= 1:
        return True
    else:
        return False

def NhapVaDem():
    count = 0
    print('Nhap day so:') 
    while True:
        n = int(input())
        if SoHopLe(n):
            break
        if LaSoNguyenTo(n):
            count += 1
    return count

def InKQ(kq):
    print(f'Co {kq} so nguyen to')   
kq = NhapVaDem()
InKQ(kq)
