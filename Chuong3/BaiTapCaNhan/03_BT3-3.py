
x = float(input("x= "))
y = float(input("y= "))
ch = input("Phep toan: ")

if ch == '+':
    ket_qua = x + y
elif ch == '-':
    ket_qua = x - y
elif ch == '*':
    ket_qua = x * y
elif ch == '/':
    if y == 0:
        print("Khong hop le")
    else:
        ket_qua = x / y
else:
    print("Khong hop le")

if 'ket_qua' in locals():
    print(f"{x}{ch}{y}={ket_qua}")






