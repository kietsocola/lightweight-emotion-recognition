import matplotlib.pyplot as plt  # khai báo thư viện vẽ pyplot
import math

# Tạo đối tượng vòng tròn
circle = plt.Circle((0, 0), 1, color='g', fill=False)

# Lấy figure và vùng vẽ
fig, ax = plt.subplots(figsize=(6, 6))

# Vẽ điểm tại tâm (0,0)
plt.plot(0, 0, 'o', color=(0.9, 0.9, 1.0), alpha=0.8)

# Thêm vòng tròn vào vùng vẽ
ax.add_patch(circle)

# Tính tọa độ điểm trên đường tròn
x = 0.75
y = math.sqrt(1 - (x ** 2))  # y = sqrt(1 - x^2)

# Vẽ mũi tên từ gốc tọa độ đến điểm (x, y)
plt.arrow(0, 0, x, y, head_width=0.05, head_length=0.05, color='r')

# Thiết lập giới hạn trục
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Lưu hình ảnh
plt.savefig('pi.png')

# Hiển thị đồ thị
plt.show()

import numpy as np

def calc_pi_monte_carlo(n=100):
    pi = 0  # Khởi tạo biến pi

    # Phát sinh n cặp điểm (x, y) với -1 <= x,y < 1
    a = np.random.rand(n, 2) * 2 - 1

    # Kiểm tra điều kiện x^2 + y^2 <= 1
    in_s = np.sum(a ** 2, axis=1) <= 1

    # Tính tổng số điểm thuộc hình tròn
    n_s = np.sum(in_s)

    # Tính số pi theo phương pháp Monte Carlo
    pi = 4 * n_s / n
    
    return pi

import math

# Gọi hàm với các giá trị n khác nhau và hiển thị kết quả
print("epsilon(n=100): ", calc_pi_monte_carlo(n=100) - math.pi)
print("epsilon(n=100): ", calc_pi_monte_carlo(n=100) - math.pi)
print("epsilon(n=10000): ", calc_pi_monte_carlo(n=10000) - math.pi)
print("epsilon(n=10000): ", calc_pi_monte_carlo(n=10000) - math.pi)
print("epsilon(n=1000000): ", calc_pi_monte_carlo(n=1000000) - math.pi)
print("epsilon(n=1000000): ", calc_pi_monte_carlo(n=1000000) - math.pi)

