# Tìm số nguyên tố
n=int(input('n='))
if n>1:
    for i in range(2,n):
        if n % i == 0:
             print(f'{n} Khong la so nguyen to')
             break # Đủ điều kiện thì các câu lệnh sau dừng hoạt động
    else:
        print(f'{n} La so nguyen to')
else:
    print(f'{n} Khong la so nguyen to')
