def NgayKyDieu():
    y=1910
    d=1
    m=1
    for y in range(1910,2000):
        Y=y%100
        for m in range(1,8):
            if y%4==0 and m==2:
                for d in range(1,30):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
            elif m==2:
                for d in range(1,29):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
            elif m!=2 and m%2==0:
                for d in range(1,31):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
            elif m!=2 and m%2!=0 :
                for d in range(1,32):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
        for m in range(8,13):
            if m%2==0:
                for d in range(1,32):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
            if m%2!=0:
                for d in range(1,31):
                    if d*m==Y:
                        print(f'Ngay ky dieu:{d}/{m}/{y}')
NgayKyDieu()               
            
        