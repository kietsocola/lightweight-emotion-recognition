s = input("Mời bạn nhập chuỗi ký số s: ")

en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Kiểm tra chuỗi nhập vào có hợp lệ không
if s.lower() not in en:
    print("Chuỗi vừa nhập không hợp lệ!")
else:
    print("Chuỗi vừa nhập hợp lệ!")
    p = en.index(s.lower())  # Lấy vị trí của chuỗi trong danh sách `en`
    print(f'"{s}" biểu diễn cho số "{num[p]}" và ứng với tiếng Việt "{vi[p]}"')
