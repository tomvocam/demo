def Nhap():
    n=int(input('n='))
    return n
def NhapvaDem(n):
    count=0
    for i in range(n):
        t=int(input())
        if t%2==0 and t!=0:
            count+=1
    return count
def inkq(count):
    print('So chu so chan la:',count)
n=Nhap()
print(f'Nhap {n} so nguyen:')
count=NhapvaDem(n)
inkq(count)