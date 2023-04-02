# def Nhap():
#     a=input('number:')
#     if a.isdigit()==True:
#         return int(a)
#     return a
# def int2hex(a):
#     if Nhap():
#         return int(a)
#         for i in range(1,10):
#             if a==i:
#                 print(a)
#     elif Nhap():
#         return a
#         for i in range(10,16):
#             if a==10:
#                 print('A')
#             elif a==11:
#                 print('B')
#             elif a==12:
#                 print('C')
#             elif a==13:
#                 print('D')
#             elif a==14:
#                 print('E')
#             elif a==15:
#                 print('F')
#             else:
#                 print('Không hợp lệ.')
# def hex2int(a):
#     for i in range(1,10):
#         if a==i:
#             print(a)
#     if i=='A':
#         print('10')
#     elif i=='B':
#         print('11')
#     elif i=='C':
#         print('12')
#     elif i=='D':
#         print('13')
#     elif i=='E':
#         print('14')
#     elif i=='F':
#         print('15')
#     else:
#         print('Không hợp lệ.')
# a=Nhap()
# int2hex(a)
# hex2int(a)
def Nhap():
    s=input("Nhap:")
    bi=int(input("He co so cua du lieu nhap:"))
    bo=int(input("He co so muon doi:"))
    if bi>16 or bo>16 or bi<2 or bo<2:
        print("Khong hop le! Vui long nhap lai")
        bi=int(input("He co so cua du lieu nhap:"))
        bo=int(input("He co so muon doi:"))
    return s,bi,bo
def baseto10(s):
    if bi==16:
        h2i=s
        kq=hex2int(h2i)
    if bi==2:
        ttt=s
        kq=two2ten(ttt)
    return kq
def ten2b(s):
    if bo==16:
        i2h=s
        kq=int2hex(i2h)
    if bo==2:
        yyy=s
        kq=ten2two(yyy)
    return kq
def giao(s):
    if bi==16 and bo==2:
        h2i=s
        gi=hex2int(h2i)
        kq=ten2two(gi)
    if bi==2 and bo==16:
        ttt=s
        gi=two2ten(ttt)
        kq=int2hex(gi)
    return kq
# bai 98
def hex2int(h2i):
    try:  i= int(h2i,16)
    except: i='Khong hop le!'
    return i
def int2hex(i2h):
    if 0<=i2h<=9: h=i2h
    elif 10<=i2h<=15:
        if i2h==10: h='A'
        if i2h==11: h='B'
        if i2h==12: h='C'
        if i2h==13: h='D'
        if i2h==14: h='E'
        if i2h==15: h='F'
    else: h='Khong hop le!'
    return h
#bai77
def two2ten(ttt):
    d_num = 0
    m = 1
    b_len = len(str(ttt))
    for k in range(b_len):
        rem = ttt%10
        d_num = d_num + (rem * m)
        m = m * 2
        ttt = int(ttt/10)
#bai78
def ten2two(yyy):
    st=[]
    while q!=0:
        r=q%2
        st.append(r)
        q=q//2
    a=""
    while st!=[]:
        a=a+str(st.pop())
    return a
s,bi,bo=Nhap()
def kqc(bi,bo):
    if bo==10: kqcc=baseto10(s)
    elif bi==10:kqcc=ten2b(s)
    else: kqcc=giao(s)
    print(s,"tu he co so",bi,"sang he co so",bo,"la:",kqcc)
s,bi,bo=Nhap()
kqc(bi,bo)
    