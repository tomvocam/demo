# Số ngày nghỉ và xếp loại của nhân viên

so_ngay_nghi = int(input(""))

# # Kiểm tra số ngày nghỉ có hợp lệ hay không ( mở rộng )
# if so_ngay_nghi < 0:
#     print("So ngay nghi khong hop le.")
# else:
if so_ngay_nghi == 0:
    print("Xep loai A")
elif so_ngay_nghi < 2:
    print("Xep loai B")
elif so_ngay_nghi < 4:
    print("Xep loai C")
else:
    print("Xep loai D")


