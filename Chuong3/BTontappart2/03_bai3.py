# Tìm số tự nhiên nguyen duong có bao nhiêu chữ số
n=int(input('n='))
temp = n #  lưu giá trị của n
count=0
while temp > 0: 
    count += 1
    temp//=10 # Chia 10 để có số tiếp theo
print('So',n,'co',count,'chu so')