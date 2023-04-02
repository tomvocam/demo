import re # khai bao re để có câu re.splitsplit
def nhap():
    a=str(input())
    A=re.split("[.!?]",a) # để tách 1 chuỗi thành các list
# Khi gặp một dấu trong đó thì sẽ tách
    return A,a
def viet_hoa(A,a):
    D=[]
    for i in range(0,len(A)):
        A[i]=A[i].strip() 
        # loại bỏ khoảng trắng đầu cuối trong A[i]
        B=A[i].capitalize()
        if len(a)>len(A[i]):
            C=B+a[len(A[i])]
        else:
            C=B
        a=a[(len(C)+1):] # lấy từ độ dài phần c trở đi
        C=C.replace("i","I") # Biến i thành I
        # biến a sẽ thay đổi mỗi khi i tăng lên 1
        D.append(C) # Thêm vào cuối chuỗi
    return ' '.join(D) # dùng để đưa cái list thành 1 str
def InKQ(D):
    print(D,end="")
A,a=nhap()
D=viet_hoa(A,a)
InKQ(D)
    