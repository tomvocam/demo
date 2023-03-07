# 3 cạnh tam giác và tính diện tích
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and b+c>a and c+a>b:
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    s=round(S,3)
    print(f'Dien tich={s}')
else:
    print('Khong hop le')