# Khởi tạo biến đếm số âm và số dương
count_positive = 0
count_negative = 0

# Nhập dãy số từ người dùng
while True:
    n = int(input("Nhập một số nguyên (nhập số 0 để kết thúc): "))
    if n == 0:
        break
    elif n > 0:
        count_positive += 1
    else:
        count_negative += 1

# In ra kết quả
print("Số dương đã nhập:", count_positive)
print("Số âm đã nhập:", count_negative)
