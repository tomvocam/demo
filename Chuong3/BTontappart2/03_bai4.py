while True: 
    a = float(input("a=: "))
    b = float(input("b=: "))
    op = input("Nhap toan tu (+, -, *, /): ") 
    
    # Kiểm tra toán tử và thực hiện phép tính 
    if op == "+":
        result = a + b
        print(f'{a}+{b}={result}')
    elif op == "-":
        result = a - b
        print(f'{a}-{b}={result}')
    elif op == "*":
        result = a * b
        print(f'{a}*{b}={result}')
    elif op == "/":
        if b==0:
            print('Khong the chia cho so 0.')
            continue
        else:
             result = a / b
             print(f'{a}/{b}={result}')
    else:
        print("Toan tu khong hop le.")
        continue  # Quay lại vòng lặp while
    print("Kết quả: ", result)   
    # tiếp tục hay không
    choice = input("Tiep tuc (nhap T hoac t đe dung): ")
    if choice.lower() == "t":
        break  # Thoát khỏi vòng lặp while


