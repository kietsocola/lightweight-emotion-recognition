# Nhập dữ liệu
n = int(input("Mời bạn nhập số nguyên n: "))

# Xử lý
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
if n == 1:
    lant = True
else:
    i = 2
    lant = True
    while i * i <= n:
        if n % i == 0:
            lant = False
            print(i)
            break
        i = i + 1  # Tăng i lên 1 đơn vị

# Xuất dữ liệu
if lant:
    print(f'{n} là số nguyên tố.')
else:
    print(f'{n} không là số nguyên tố.')
