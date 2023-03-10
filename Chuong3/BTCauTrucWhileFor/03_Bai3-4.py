# Câu a while
# i = 9
# while i >= 1:
#     j = i
#     while j >= 1:
#         print("$", end="")
#         j -= 1
#     print()
#     i -= 1
# Câu a while cách 2
# i=9
# while i>0:
#     print(i*'$')
#     i-=1
#Câu a for cách 2
# for i in range(9,0,-1):
#     print(i*'$')
# Câu a for
# for i in range(9, 0, -1):
#     for j in range(i, 0, -1):
#         print("$", end="")
#     print()

# Câu b while
# i=1
# while i<10:
#     print(" "*(9-i)+"*"*(2*i-1))
#     i+=1
    
# Câu b for
for i in range(1, 10): # có thể cho n =10 rồi chạy từ 1-n
    print(" "*(9-i) + "*"*(2*i-1))

