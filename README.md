# 📘 Đồ án môn học: Phương pháp nghiên cứu khoa học (PPNCKH)

## 📝 Giới thiệu chung

Đây là repo chứa toàn bộ nội dung đồ án môn học **Phương pháp nghiên cứu khoa học**. Repo được tổ chức thành các thư mục tương ứng với các bài tập hàng tuần do giảng viên giao, các tài liệu phục vụ nghiên cứu, cũng như file ghi lại quá trình làm việc của từng thành viên trong nhóm.

## 🎯 Giới thiệu dự án

Dự án **"Nhận diện biểu cảm khuôn mặt trong điều kiện ánh sáng yếu sử dụng CNN nhẹ kết hợp kỹ thuật tăng cường dữ liệu thích ứng"** tập trung vào việc cải thiện độ chính xác của mô hình trong môi trường ánh sáng không ổn định — một thách thức lớn trong các ứng dụng thị giác máy tính thực tế.

Trong dự án này, chúng tôi sử dụng **MobileNetV3**, một mô hình CNN nhẹ và hiệu quả, phù hợp với cả các thiết bị có tài nguyên hạn chế như điện thoại thông minh hoặc hệ thống nhúng.

Mô hình được huấn luyện trên tập dữ liệu **FER2013**, một tập dữ liệu phổ biến cho nhận diện biểu cảm khuôn mặt, bao gồm các biểu cảm như:
- Vui 😄
- Buồn 😢
- Giận dữ 😠
- Ngạc nhiên 😲
- Chán nản 😐
- Sợ hãi 😨
- Kinh tởm 🤢

Để tăng cường khả năng nhận diện trong điều kiện ánh sáng yếu, chúng tôi áp dụng các **kỹ thuật tiền xử lý ảnh và tăng cường dữ liệu thích ứng**, bao gồm:
- 📈 **Gamma Correction**: giúp điều chỉnh độ sáng tổng thể của hình ảnh
- 🧮 **Histogram Equalization**: cải thiện độ tương phản trong các vùng tối và sáng

Các kỹ thuật này không chỉ cải thiện chất lượng ảnh đầu vào mà còn giúp mô hình học tốt hơn các đặc trưng khuôn mặt trong nhiều điều kiện ánh sáng khác nhau.

---

> _Mục tiêu của dự án là xây dựng một mô hình nhẹ, chính xác, và hoạt động hiệu quả trong môi trường thực tế, đặc biệt khi dữ liệu đầu vào có chất lượng kém do ánh sáng yếu._

## 📁 Cấu trúc thư mục

### Thư mục chính:

| Thư mục / File          | Mô tả                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| `.ipynb_checkpoints`    | Thư mục tạm sinh ra bởi Jupyter Notebook để lưu checkpoint tự động.                   |
| `anaconda_projects`     | Các project thực hiện trong môi trường Anaconda.                                          |
| `Bài 3`, `Bài 4`    | Các bài tập tuần theo thứ tự giảng viên giao.                                           |
| `bai_tap_python`        | Tổng hợp các bài tập Python đã thực hiện.                                              |
| `Bai5_KhaoSatDuLieuEDa` | Nội dung bài 5: Khảo sát dữ liệu bằng phương pháp EDA (Exploratory Data Analysis).    |
| `BaiBaoDaDoc`           | Thư mục lưu trữ các bài báo đã đọc và nghiên cứu trong quá trình làm đồ án. |
| `Đề cương`          | File đề cương đồ án, kế hoạch thực hiện hoặc tổng quan nội dung.                  |
| `EDA_FER2013/eda.ipynb` | Notebook phân tích dữ liệu EDA trên bộ dữ liệu FER2013.                                 |
| `ThietKeThuatToan/test` | Thư mục chứa nội dung thiết kế thuật toán và file kiểm thử.                          |

---

## 📄 Các file quan trọng

| File                                | Mô tả                                                                          |
| ----------------------------------- | -------------------------------------------------------------------------------- |
| `.gitignore`                      | File cấu hình Git để bỏ qua các file/thư mục không cần theo dõi.      |
| `[Tutorial] EDA-Python (1).ipynb` | Notebook hướng dẫn sử dụng Python cho phân tích dữ liệu.                |
| `README.md`                       | Tài liệu giới thiệu tổng quan về repo và đồ án (chính là file này). |
| `Tracking_Kiet.md`                | File theo dõi công việc, tiến độ của bạn**Kiệt**.                 |
| `Tracking_Lam.md`                 | File theo dõi công việc, tiến độ của bạn**D. Lâm**.               |
| `Tracking_Loc.md`                 | File theo dõi công việc, tiến độ của bạn**Lộc**.                  |
| `Tracking_PLam.md`                | File theo dõi công việc, tiến độ của bạn**P. Lâm**.               |

---

## Phân chia nhiệm vụ

Mọi vấn đề về chia nhiệm vụ cho từng thành viên được thực hiện ở [file excel](https://docs.google.com/spreadsheets/d/1fQEhZhOme_cUPzWFHYGgAEzErR-zbi63u4UeUeJ06Mo/edit?gid=700579882#gid=700579882) (file excel cập nhật hàng tuần)


## Kế hoạch thực nghiệm

Mọi vấn đề về kế hoạch thực nghiệm cho dự án cuối môn được thực hiện ở [file excel](https://docs.google.com/spreadsheets/d/1BYEiQDNeR3SQME8fLpjtJrljtBMBBZSAvlPewkP45Yo/edit?gid=0#gid=0) (file excel cập nhật hàng tuần)


## 👥 Thành viên nhóm 17

| Họ và tên           | Email                                                | GitHub                                                  | Website cá nhân                                                                      |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Nguyễn Hữu Lộc      | [lockbkbang@gmail.com](mailto:lockbkbang@gmail.com)     | [github.com/LocNguyenSGU](https://github.com/LocNguyenSGU) | [locnguyensgu.github.io/nguyenhuuloc2k4](https://locnguyensgu.github.io/nguyenhuuloc2k4/) |
| Nguyễn Đức Duy Lâm | [duylam468213@gmail.com](mailto:duylam468213@gmail.com) | [github.com/duylam15](https://github.com/duylam15)         | [porfolio-cyan-nine.vercel.app](https://porfolio-cyan-nine.vercel.app/)                   |
| Mai Phúc Lâm    | [lamkbvn@gmail.com](mailto:lamkbvn@gmail.com)         | [github.com/lamkbvn](https://github.com/lamkbvn) | [lamkbvn.github.io/trang-ca-nhan/](https://lamkbvn.github.io/trang-ca-nhan/)                             |
| Tên thành viên 4    | [email4@example.com](mailto:email4@example.com)         | [github.com/username4](https://github.com/username4)       | [gắn link vô](#)                                                                        |

## ✅ Ghi chú

- Mỗi thư mục tương ứng với một bài học, nhiệm vụ hoặc nội dung thực hành được giao theo tuần.
- Các file `Tracking_*.md` được sử dụng để ghi lại tiến độ cá nhân, ghi chú công việc hoặc các vấn đề gặp phải.
- Các file notebook (`.ipynb`) là nơi triển khai, thử nghiệm và trình bày quá trình phân tích dữ liệu, xây dựng thuật toán,...

---

> *Repo được cập nhật liên tục trong quá trình thực hiện đồ án.*
