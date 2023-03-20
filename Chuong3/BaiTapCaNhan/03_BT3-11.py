# Khởi tạo biến đếm số âm và số dương
count_positive = 0
count_negative = 0

# Nhập dãy số từ người dùng
while True:
    n = int(input(""))
    if n == 0:
        break
    elif n > 0:
        count_positive += 1
    else:
        count_negative += 1

# In ra kết quả
print(f"{count_positive} so duong")
print(f"{count_negative} so am")
