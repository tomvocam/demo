def Nhap():
    n=int(input('n='))
    return n
def inkq(n):
    for i in range(1,n+1):
        if i %2 == 0:
            print(i,end=' ')              
while True:
    n=Nhap()
    inkq(n)
    print()
    choice = input('Tiep tuc khong?')
    if choice.lower()=='k':
        break   