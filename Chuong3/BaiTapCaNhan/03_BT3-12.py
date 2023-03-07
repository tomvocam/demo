# Tạo dictionary để ánh xạ các chữ số với chữ cái tương ứng
digits = {
    "0": "A",
    "1": "B",
    "2": "C",
    "3": "D",
    "4": "E",
    "5": "F",
    "6": "G",
    "7": "H",
    "8": "K",
    "9": "L"
}

n = int(input("Nhập số nguyên n (0<=n<=9999): "))

# Chuyển số nguyên n thành chuỗi và mã hóa từng ký tự
encoded = ""
for digit in str(n):
    encoded += digits[digit] + ""

print(encoded)
