# Câu a
# n=int(input('n='))    
# for i in range (1, n+1):
#     if n<1:
#         break
#     print(i)

# Câu b
# n=int(input('n='))
# count=0   
# for i in range (1, n+1):
#     if i<1:
#         break
#     print(i, end=' ')
#     count += 1
#     if count == 5:
#         print() # Xuống dòng
#         count=0

# Câu c
n=int(input('n='))  
# while n < 1:
#     print('Không hợp lệ.')
#     n=int(input('Nhập n: '))


for i in range(1, n+1):
    if i<1:
        break
    for j in range(1, n+1):
        print(j, end=' ') 
    print()