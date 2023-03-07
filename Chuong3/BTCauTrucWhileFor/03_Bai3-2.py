# Lặp while
n=int(input('nhap n:'))
i=1
while n<1 or n>50:
    print('Nhap lai')
    n=int(input('n='))
while i<=n:
    if i%10==0:
        print(i,end='\n')
    else:
        print(i,end=' ')
    i+=1
    
# Lặp for
# n = int(input('Nhập n: '))
# while n < 1 or n > 50:
#     print('Nhập lại')
#     n = int(input('n = '))

# for i in range(1, n+1):
#     if i % 10 == 0:
#         print(i, end='\n')
#     else:
#         print(i, end=' ')
