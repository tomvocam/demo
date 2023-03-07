#Tính giai thừa
n=int(input('n='))
giaithua=1
if n==0:
    print(f'{n}!=1')
else:
    for i in range(1, n+1): # Chạy từ 1 đến n
         giaithua *= i  #giaithua = giaithua * i
    print(f'{n}!={giaithua}')

