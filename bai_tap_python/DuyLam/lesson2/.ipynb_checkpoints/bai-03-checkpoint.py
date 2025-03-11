# Nhập dữ liệu
a = int(input('Mời bạn nhập hệ số a: '))
b = int(input('Mời bạn nhập hệ số b: '))

# Xử lý
flag, x = None, None

if a == 0:  # Trường hợp a = 0
    if b == 0:  # 0 = 0 --> phương trình có vô số nghiệm
        flag = -1  # Vô số nghiệm
    else:  # b ≠ 0 --> phương trình vô nghiệm
        flag = 0  # Vô nghiệm
else:  # a ≠ 0: phương trình có nghiệm x = -b / a
    flag = 1
    x = -b / a

# Xuất dữ liệu
s = f'Phương trình {a}x + {b} = 0'
if flag == -1:
    print(f'{s} có vô số nghiệm.')
elif flag == 0:
    print(f'{s} vô nghiệm.')
else:
    print(f'{s} có 1 nghiệm x = {x:.2f}.')
