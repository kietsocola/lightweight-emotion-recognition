import numpy as np

# Tạo ma trận a
a = np.array([[197, 123, 114, 153],
              [100, 191, 101, 148],
              [116, 154, 135, 155],
              [173, 151, 137, 152],
              [177, 178, 107, 174],
              [169, 195, 136, 133]])

print("Ma trận a:\n", a)

# a. Ma trận chuyển vị
a_t = a.T

# b. Phần tử dòng 2, cột 3
v_23 = a[2, 3]

# c. Trích xuất các dòng
d_0, d_last, d_2 = a[0, :], a[-1, :], a[2, :]

# d. Trích xuất các cột
c_l1, c_0 = a[:, -2], a[:, 0]

# e. Đảo cột
dao_cot = a[::-1, :]

# f. Phép toán trên ma trận
tong_dong = np.sum(a, axis=1)  # Tổng từng dòng
tb_cot = np.mean(a, axis=0)     # Trung bình từng cột

# In kết quả
print(f"\na. Ma trận chuyển vị:\n{a_t}")
print(f"\nb. Phần tử tại dòng 2, cột 3: {v_23}")
print(f"\nc. Trích xuất các dòng:")
print(f"   + Dòng đầu   : {d_0}")
print(f"   + Dòng cuối  : {d_last}")
print(f"   + Dòng hai   : {d_2}")
print(f"\nd. Trích xuất các cột:")
print(f"   + Cột kế cuối: {c_l1}")
print(f"   + Cột đầu    : {c_0}")
print(f"\ne. Đảo các giá trị trên từng cột:\n{dao_cot}")
print(f"\nf. Phép toán trên ma trận:")
print(f"   + Tổng từng dòng    : {tong_dong}")
print(f"   + Trung bình từng cột: {tb_cot}")

# Tạo ma trận A, B (4x3) và X (3x4)
A = np.random.randint(1, 6, (4, 3))
B = np.random.randint(1, 6, (4, 3))
X = np.random.randint(1, 6, (3, 4))

# Tính toán với ma trận
AB_add = A + B
AB_sub = A - B
AB_mul = A * B
Y = np.matmul(A, X)

print("\n===== Ma trận A, B, X =====")
print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"X:\n{X}")

print("\n===== Phép toán trên ma trận A và B =====")
print(f"A + B:\n{AB_add}")
print(f"A - B:\n{AB_sub}")
print(f"A * B:\n{AB_mul}")

print("\n===== Phép nhân ma trận Y = A * X =====")
print(f"Y = A * X (shape {A.shape} x {X.shape} = {Y.shape}):\n{Y}")

# Giải hệ phương trình Ax = y
A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])
y = np.array([2, 5, -3])

# Cách 1: Dùng np.linalg.solve
# x = np.linalg.solve(A, y)

# Cách 2: Dùng ma trận nghịch đảo
A_inv = np.linalg.inv(A)
x = np.dot(A_inv, y)
yy = np.matmul(A, x)
diff = np.linalg.norm(yy - y)  # ||yy - y||_2

print("\n===== Giải hệ phương trình Ax = y =====")
print(f"A:\n{A}")
print(f"y: {y}")
print(f"Nghiệm x: {x}")
print(f"Kiểm tra: yy = Ax = {yy} ==> ||yy - y||_2 = {diff:.2f}")
