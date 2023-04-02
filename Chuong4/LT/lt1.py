def Nhap():
    x=int(input('x= '))
    global y   
    y=5
    return y+x
kq=Nhap()
print('y=',y)
print('kq=',kq)