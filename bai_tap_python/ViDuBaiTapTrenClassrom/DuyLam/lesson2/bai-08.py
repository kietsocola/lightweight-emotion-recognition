import random

def NhapMang():
    """
    Input:
    Ban phim = 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
    Output:
    a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    """
    line = input("Moi ban nhap mang (cach nhau khoang trang): ")
    a = [int(x) for x in line.split()]
    return a

def XuatMang(a):
    """
    Input:
    a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    Output:
    Mang co 16 phan tu: 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
    """
    print(f'Mang co {len(a)} phan tu: {" ".join(map(str, a))}')

def SinhNgauNhien(n, vmin=-10, vmax=10):
    """
    Sinh ngẫu nhiên mảng có n phần tử trong khoảng vmin đến vmax.
    """
    return [random.randint(vmin, vmax) for _ in range(n)]

def DemTongChanLe(a):
    """
    Tính tổng mảng, số lượng số chẵn và số lượng số lẻ.
    """
    tong = sum(a)
    sochan = sum(1 for x in a if x % 2 == 0)
    sole = len(a) - sochan
    return tong, sochan, sole

def DayChanLe(a):
    """
    Tách danh sách số chẵn và số lẻ từ mảng a.
    """
    achan = [x for x in a if x % 2 == 0]
    ale = [x for x in a if x % 2 != 0]
    return achan, ale

# --- Chạy thử ---
a = NhapMang()
XuatMang(a)

b = SinhNgauNhien(30, -10, 10)
print("Mảng ngẫu nhiên:", b)

tong, sochan, sole = DemTongChanLe(b)
print(f"Tổng: {tong}, Số chẵn: {sochan}, Số lẻ: {sole}")

achan, ale = DayChanLe(b)
print(f"Chan: {achan}\nLe: {ale}")
