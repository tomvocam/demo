# Kết quả xếp loại của học sinh
# Nhập điểm thi 3 môn
toan = float(input(""))
ly = float(input(""))
hoa = float(input(""))

# Tính điểm trung bình
diem_trung_binh = (toan*2 + ly*3 + hoa)/6

# Xếp loại
if diem_trung_binh < 3:
    xep_loai = "Kem"
elif diem_trung_binh < 5:
    xep_loai = "Yeu"
elif diem_trung_binh < 6:
    xep_loai = "Trung binh"
elif diem_trung_binh < 7:
    xep_loai = "Trung binh Kha"
elif diem_trung_binh < 8:
    xep_loai = "Kha"
elif diem_trung_binh < 9:
    xep_loai = "Gioi"
else:
    xep_loai = "Xuat sac"

print(xep_loai)




