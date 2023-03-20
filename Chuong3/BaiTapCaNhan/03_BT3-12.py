# Tạo dictionary để ánh xạ các chữ số với chữ cái tương ứng
# digits = {
#     "0": "A",
#     "1": "B",
#     "2": "C",
#     "3": "D",
#     "4": "E",
#     "5": "F",
#     "6": "G",
#     "7": "H",
#     "8": "K",
#     "9": "L"
# }

# n = int(input("Nhập số nguyên n (0<=n<=9999): "))

# mahoa = ""
# for digit in str(n):
#     mahoa += digits[digit] + ""

# print(encoded)
#C2
# n=int(input())
# mahoa=['A','B','C','D','E','F','G','H','K','L']

# while n>=0 and n<=9999:
#     if n<10:
#         print(mahoa[n])   
        
#     elif n>=10 and n<100:
#         print(mahoa[n//10],mahoa[n%10],sep='')
#     elif n>=100 and n<1000:
#         i=n//10 #vd: n=123 => i=12
#         print(mahoa[i//10],mahoa[i%10],mahoa[n%10],sep='')
#     elif n>=1000 and n<=9999: #vd n=1234
#         i=n//100  
#         j=n%100  
#         print(mahoa[i//10],mahoa[i%10],mahoa[j//10],mahoa[j%10],sep='')
#     n=n*-1
#C3
# n = int(input())
# mahoa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L']

# if n < 10:
#     print(mahoa[n])
# elif n < 100:
#     print(f'{mahoa[n//10]}{mahoa[n%10]}')
# elif n < 1000:
#     print(f'{mahoa[n//100]}{mahoa[n//10%10]}{mahoa[n%10]}')
# elif n < 10000:
#     print(f'{mahoa[n//1000]}{mahoa[n//100%10]}{mahoa[n//10%10]}{mahoa[n%10]}')
    
#C4
n = int(input())
n_str = str(n)
mh = ''
for char in n_str:
    if 0>=n or n>9999:
        break
    if char == '0':
        mh += 'A'
    elif char == '1':
        mh += 'B'
    elif char == '2':
        mh += 'C'
    elif char == '3':
        mh += 'D'
    elif char == '4':
        mh += 'E'
    elif char == '5':
        mh += 'F'
    elif char == '6':
        mh += 'G'
    elif char == '7':
        mh += 'H'
    elif char == '8':
        mh += 'K'
    elif char == '9':
        mh += 'L'
print(mh)

