import math

def NhapDuLieu():
    """
    Input:
    Bàn phím = 1 5 6
    Output:(a, b, c) --> (1, 5, 6)
    """
    is_valid = False
    while not is_valid:
        try:
            line = input("Mời bạn nhập hệ số a, b, c: ")
            a_snum = line.split()
            a, b, c = int(a_snum[0]), int(a_snum[1]), int(a_snum[2])
            is_valid = True
        except:
            print("Dữ liệu không hợp lệ, vui lòng nhập lại!")
    return a, b, c

def GiaiPhuongTrinhBac2(a, b, c):
    """
    Input: a, b, c
    Output:
    + flag = -1 (VSN), 0 (VN), k (k nghiệm)
    + () --> flag = -1, 0
    + (x) --> flag = 1
    + (x1, x2) --> flag = 2
    """
    flag = None
    x = ()

    if a == 0:  # Phương trình bậc 1: bx + c = 0
        if b == 0:  # c = 0
            if c == 0:  # 0 = 0: Vô số nghiệm
                flag = -1
            else:  # c ≠ 0: Vô nghiệm
                flag = 0
        else:  # b ≠ 0: bx + c = 0 ⇒ x = -c / b
            flag = 1
            x = (-c / b,)
    else:  # Phương trình bậc 2: ax^2 + bx + c = 0
        delta = b * b - 4 * a * c
        if delta < 0:
            flag = 0  # Vô nghiệm
        elif delta == 0:  # Nghiệm kép x = -b / (2a)
            flag = 1
            x = (-b / (2 * a),)
        else:  # Hai nghiệm phân biệt
            flag = 2
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            x = (x1, x2)
    
    return flag, x

# Kiểm tra chương trình
a, b, c = NhapDuLieu()

# Gọi hàm giải phương trình
flag, x = GiaiPhuongTrinhBac2(a, b, c)

# Xuất kết quả
s = f'Phương trình bậc 2 {a}x^2 + {b}x + {c} = 0'
if flag == -1:
    print(f'{s} có vô số nghiệm!')
elif flag == 0:
    print(f'{s} vô nghiệm!')
elif flag == 1:
    print(f'{s} có một nghiệm kép, x = {x[0]}!')
elif flag == 2:
    print(f'{s} có 2 nghiệm phân biệt, x1 = {x[0]}, x2 = {x[1]}!')
