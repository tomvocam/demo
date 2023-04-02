# def from_base_n(number, base): #số cần chuyển đổi và hệ số
#     #Chuyển đổi số từ bất kỳ hệ cơ số nào sang hệ cơ số 10
#     result = 0 # Lưu kết quả
#     power = 0 # Tính giá trị
#     for digit in reversed(number): #reversed để đảo ngược thứ tự các chữ số
#         value = int(digit, base) # trả về giá trị digit trong hệ số base
#         result += value * (base ** power)#Tính giá trị
#         power += 1
#     return result

# def to_base_n(number, base): #số cần chuyển đổi và hệ số
#     #Chuyển đổi số từ hệ cơ số 10 sang bất kỳ hệ cơ số nào
#     if number == 0:
#         return '0'
#     result = ''
#     while number > 0:
#         if base == 16:
#             result = hex(number)
#             break
#         digit = number % base
#         result = str(digit) + result
#         number //= base
#     return result

# def main():
#     #Chương trình chính
#     from_base = int(input("Nhập hệ cơ số ban đầu (từ 2 đến 16): "))
#     if from_base < 2 or from_base > 16:
#         print("Lỗi: Hệ cơ số không hợp lệ")
#         return
#     to_base = int(input("Nhập hệ cơ số muốn chuyển đổi sang (từ 2 đến 16): "))
#     if to_base < 2 or to_base > 16:
#         print("Lỗi: Hệ cơ số không hợp lệ")
#         return
#     number = input("Nhập số cần chuyển đổi: ")
#     try:
#         decimal = from_base_n(number, from_base)
#         result = to_base_n(decimal, to_base)
#         print(f"{number} trong hệ cơ số {from_base} tương đương với {result} trong hệ cơ số {to_base}")
#     except ValueError:
#         print("Lỗi: Số không hợp lệ")

# if __name__ == '__main__':
#     main()

    
      
        
    

















