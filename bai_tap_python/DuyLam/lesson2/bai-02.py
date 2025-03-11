# Nhập dữ liệu
t = int(input('Nhap vao tong so giay: '))
# Xử lý
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
hh = t // (60*60)
mm = (t % (60 * 60)) // 60
ss = t % 60
# Xuất dữ liệu
print(f'{t} giay co dang {hh}:{mm}:{ss}')