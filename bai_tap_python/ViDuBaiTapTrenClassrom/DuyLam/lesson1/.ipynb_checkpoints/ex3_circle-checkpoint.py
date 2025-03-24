import math

print("Chương trình tính chu vi và diện tích hình tròn")

# Nhập bán kính r
r = float(input("Nhập bán kính r: "))

# Tính chu vi và diện tích
cv = 2 * math.pi * r
dt = math.pi * r ** 2

# Hiển thị kết quả
print("Chu vi hình tròn: %.2f" % cv)
print("Diện tích hình tròn: %.2f" % dt)
