# Vòng lặp bằng while
# n = 0
# while True:
#     n = int(input(""))
#     if 2 <= n <= 50:
#         break
#     print("")

# count = 1  # Số lượng số chẵn đã in ra
# i = 1  # Số chẵn đang xét

# while count < n:
#     if i % 2 == 0:  # Nếu số chẵn
#         print(i, end=" ")
#         count += 2
#     i += 1

# Vòng lặp bằng for    
# n = int(input("Nhập n: "))
# while n < 2 or n > 50:
#     print("Số n không hợp lệ, vui lòng nhập lại!")
#     n = int(input("Nhập n: "))

# count = 0  # Biến đếm số lượng số chẵn đã in ra
# for i in range(n + 1):
#     if i % 2 == 0 and i>0:  # Kiểm tra số i có chẵn không
#         print(i, end=' ')
#         count += 1  # Tăng biến đếm lên 1
#         if i == n:  # Nếu đã in ra đủ n số chẵn thì dừng vòng lặp
#             break
        
#Cach 2
#  Lap While
# n=int(input(''))
# i=2
# while i<(n+1):
#     if 2>=n or n>=51:
#         break
#     print(i,end=' ')
#     i+=2
# Lap For
n=int(input(''))
for i in range(2,n+1,2):
    print(i, end=' ')


   