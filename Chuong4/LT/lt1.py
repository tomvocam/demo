def Nhap():
    n = int(input("n="))
    return n
def NhapVaDem(n):
    count = 0
    for i in range(1,n+1):
        # num=int(input())
        # num = int(input("Nhap vao so nguyen thu %d: " % (i))) # Dạng chuỗi, i chạy từ 1 đến n
        while num != 0: #num khac 0
            if (num % 10) % 2 == 0:
                count += 1
            num //= 10
    return count
def InKQ(kq):
    print("So chu so chan la: %d" % kq)
n=Nhap()
print('Nhap',n,'so nguyen:')
kq=NhapVaDem(n)
InKQ(kq)

