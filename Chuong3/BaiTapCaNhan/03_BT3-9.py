# Vòng lặp bằng while
# n = 0
# while True:
#     n = int(input("Nhập vào số nguyên n (2 <= n <= 50): "))
#     if 2 <= n <= 50:
#         break
#     print("Giá trị của n không hợp lệ. Vui lòng nhập lại.")

# count = 1  # Số lượng số chẵn đã in ra
# i = 1  # Số chẵn đang xét

# while count < n:
#     if i % 2 == 0:  # Nếu số chẵn
#         print(i, end=" ")
#         count += 2
#     i += 1

# Vòng lặp bằng for    
n = int(input("Nhập n: "))
while n < 2 or n > 50:
    print("Số n không hợp lệ, vui lòng nhập lại!")
    n = int(input("Nhập n: "))

count = 0  # Biến đếm số lượng số chẵn đã in ra
for i in range(n + 1):
    if i % 2 == 0 and i>0:  # Kiểm tra số i có chẵn không
        print(i, end=' ')
        count += 1  # Tăng biến đếm lên 1
        if i == n:  # Nếu đã in ra đủ n số chẵn thì dừng vòng lặp
            break
        
#Cach 2
##  Lap While
# n=int(input(''))
# i=0
# while 2<=i<n<=50:
#     print(i,end=' ')
#     i+=2
# Lap For
# n=int(input(''))
# for i in range(0,n+2,2):
#     if 2>=n or n>=50:
#         break
#     print(i, end=' ')


   