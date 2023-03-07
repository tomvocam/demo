so_kw=int(input('Tieu thu='))
dongia=0
if so_kw<=100:
    dongia=550*so_kw
elif so_kw<=150:
    dongia=750*(so_kw-100)+100*550
elif so_kw<=200:
    dongia=950*(so_kw-150)+100*550+50*750
else:
    dongia=1350*(so_kw-200)+100*550+50*750+950+50
thanhtien=dongia*1.1
Tien=round(thanhtien,1)
print(f'Phai tra={Tien}')





