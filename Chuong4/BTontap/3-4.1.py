def Nhap():
    n=int(input('n='))
    return n
def NhapvaDem(n):
    count=0
    print(f'Nhap {n} so nguyen:')
    for i in range(n):
        t=int(input())
        if t%2==0 and t!=0:
            count+=1
    return count
def inkq(count):
    print('So chu so chan la:',count)
n=Nhap()
count=NhapvaDem(n)
inkq(count)