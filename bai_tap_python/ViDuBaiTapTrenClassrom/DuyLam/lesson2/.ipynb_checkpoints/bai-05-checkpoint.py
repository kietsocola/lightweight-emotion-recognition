# Nhập dữ liệu
n = int(input("Mời bạn nhập số nguyên n: "))

# Xuất dữ liệu
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
a_n = range(1, n + 1)  # Sinh các số từ 1 đến n
s = 0

for i in a_n:
    if i % 2 == 0:  # Kiểm tra số chẵn
        s = s + i   # Cộng tổng các số chẵn

print(f'Tổng các số chẵn từ 1 đến {n} là {s}.')
