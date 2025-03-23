def XuLyKhongTrung(a):
    """
    Input:
    a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
    s = ['A', 'C', 'F', 'G', 'H', 'T']
    """
    s = set(a)  # Dùng set để loại bỏ trùng lặp
    return sorted(s)  # Sắp xếp theo thứ tự tăng dần

# Test
a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
b = XuLyKhongTrung(a)
print(b)  # ['A', 'C', 'F', 'G', 'H', 'T']

def DemSoLanXuatHien(a):
    """
    Input:
    a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
    dem = {'A': 2, 'G': 1, 'C': 2, 'F': 2, 'T': 1, 'H': 1}
    """
    dem = {}  # Dictionary để lưu số lần xuất hiện
    for ai in a:
        if ai not in dem:
            dem[ai] = 1
        else:
            dem[ai] += 1
    return dem

# Test
a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
b = DemSoLanXuatHien(a)
print(b)  # {'A': 2, 'G': 1, 'C': 2, 'F': 2, 'T': 1, 'H': 1}
