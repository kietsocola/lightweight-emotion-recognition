import numpy as np
import matplotlib.pyplot as plt  # Thêm import để vẽ biểu đồ

print("1. Tạo một dãy số a có N phần tử (N = 10)")

# Tạo dãy số ngẫu nhiên từ 100 đến 200, gồm 10 phần tử
a = np.array([120, 183, 160, 175, 145, 162, 190, 160, 152, 162])
print("Dãy số a:", a)

print("2. Các thao tác tính toán đơn giản với dãy số a")

# a. Bình phương các phần tử trong a
a2 = a ** 2
print("a. Bình phương a:", a2)

# b. Độ dài của dãy số a
na = len(a)
print("\nb. Độ dài của a:", na)

# c. Giá trị lớn nhất, nhỏ nhất và trung bình của a
v_max = np.max(a)
v_min = np.min(a)
v_avg = np.mean(a)
print(f"\nc. Giá trị lớn nhất: {v_max}, giá trị nhỏ nhất: {v_min}, giá trị trung bình: {v_avg:.2f}")

# d. Phương sai và độ lệch chuẩn của a
v_mean = np.mean(a)
v_var = np.var(a, ddof=1)  # Phương sai mẫu
v_std = np.std(a, ddof=1)  # Độ lệch chuẩn mẫu
print(f"\nd. Phương sai: {v_var:.2f}, độ lệch chuẩn: {v_std:.2f}")

print("3. Xử lý khác trên dãy số")

# a. Tạo dãy số x từ 1 đến 10
x = np.arange(1, 11)
print(f"a. Dãy số x: {x}")

# b. Lọc phần tử chẵn trong a và x
a_chan = a[a % 2 == 0]
x_chan = x[x % 2 == 0]
print("b. Các phần tử chẵn:")
print(f" - Dãy a: {a}")
print(f" - Phần tử chẵn trong a: {a_chan}, số lượng: {len(a_chan)}")
print(f" - Dãy x: {x}")
print(f" - Phần tử chẵn trong x: {x_chan}, số lượng: {len(x_chan)}")

# c. Tính hiệu các phần tử ở vị trí lẻ giữa a và x
v_le = np.arange(1, len(a), 2)  # Chỉ mục lẻ
a_le = a[v_le]
x_le = x[v_le]
hieu_le = a_le - x_le
kc_le = np.sqrt(np.sum(hieu_le ** 2))
print("c. Hiệu các phần tử ở vị trí lẻ:")
print(f" - Vị trí lẻ: {v_le}")
print(f" - Các phần tử ở vị trí lẻ của a: {a_le}")
print(f" - Các phần tử ở vị trí lẻ của x: {x_le}")
print(f" - Hiệu giữa a và x ở vị trí lẻ: {hieu_le}")
print(f" - Khoảng cách: {kc_le:.2f}")

# d. Tìm khoảng cách nhỏ nhất giữa tập a và x
v_min = np.min(np.abs(a[:, np.newaxis] - x))
print("\nd. Khoảng cách nhỏ nhất giữa a và x:")
print(f" - Dãy a: {a}")
print(f" - Dãy x: {x}")
print(f" - Khoảng cách nhỏ nhất: {v_min}")

print("4. Sinh dãy số ngẫu nhiên và thống kê")

# a. Sinh ngẫu nhiên số nguyên trong khoảng [1, 10], 10000 phần tử
x = np.random.randint(1, 11, 10000)
value, cnt = np.unique(x, return_counts=True)
print("a. Sinh ngẫu nhiên theo phân bố đều:")
print(f" - Giá trị: {value}")
print(f" - Số lần xuất hiện: {cnt}")

# Vẽ biểu đồ tần suất
plt.figure(figsize=(6, 6))
plt.bar(value, cnt)
plt.xlim(0, 11)
plt.ylim(0, np.max(cnt) + 10)
plt.savefig("4a.png")
plt.show()

# b. Sinh cặp (x, y) theo phân phối chuẩn
m, s2 = 1, 1
s = np.sqrt(s2)
x_min, x_max = m - 5 * s, m + 5 * s
x = np.random.rand(100) * (x_max - x_min) + x_min
y = (1 / (s * np.sqrt(2 * np.pi))) * np.exp(-((x - m) ** 2) / (2 * s2))
print("\nb. Sinh cặp (x, y) với y làm hàm phân phối chuẩn:")
print(f" - x: [{x_min:.2f}, {np.min(x):.2f}] <= max [{np.max(x):.2f}, {x_max:.2f}]")

# Vẽ biểu đồ phân phối chuẩn
plt.figure(figsize=(6, 6))
plt.scatter(x, y)
plt.savefig("4b.png")
plt.show()

# c. Sinh dãy số theo phân phối chuẩn N(1,1)
x = m + np.random.randn(100000) * s
cnt, val = np.histogram(x, bins=300, density=True)
val = (val[:-1] + val[1:]) / 2
print("\nc. Sinh dãy số theo phân phối chuẩn:")
print(f" - Độ dài: {len(x)}, min: {np.min(x):.2f}, max: {np.max(x):.2f}")

# Vẽ mật độ xác suất của phân phối chuẩn
plt.figure(figsize=(6, 6))
plt.xlim(np.min(val), np.max(val))
plt.scatter(val, cnt)
plt.show()
