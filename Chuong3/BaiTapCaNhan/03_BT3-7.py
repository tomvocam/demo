# Lặp bằng while
while True:
    n = int(input(""))
    if n < 0:
        break
    a = 1
    i = 1
    while i <= n:
        a *= i
        i += 1
    print(a)

# Lặp bằng for
# while True:
#     n = int(input(""))
#     if n < 0:
#         break
#     if n ==0:
#         print('1')
       
#     a = 1
#     for i in range(1, n+1):
#         a *= i
#     print(a)



