# Khai báo thư viện
import math
# Nhập dữ liệu
x = float(input('Moi ban nhap vao gia tri cua bien so x: '))
# Xử lý
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
f_x = x + (x ** 5) / (1 * 2 * 3 * 4 * 5) + math.sqrt(math.fabs(x)) / math.pow(x, 3.0 / 2)
# Xuất dữ liệu
print(f'Gia tri cua ham so f({x}) = {f_x: .2f}.')