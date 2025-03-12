
# Kế hoạch dự án (SCHEDULE.md)

## Tên đề tài

Nhận diện biểu cảm khuôn mặt trong điều kiện ánh sáng yếu sử dụng CNN nhẹ kết hợp kỹ thuật tăng cường dữ liệu thích ứng

## Thành viên / Thông tin liên hệ

- **[Nguyễn Hữu Lộc]**
  - **Email: [lockbkbang@gmail.com](mailto:lockbkbang@gmail.com)**
  - **GitHub: [https://github.com/LocNguyenSGU](https://github.com/LocNguyenSGU)**
  - **Website cá nhân: [https://locnguyensgu.github.io/nguyenhuuloc2k4/](https://locnguyensgu.github.io/nguyenhuuloc2k4/)**
- **[Tên thành viên 2]**
  - Email: [email2@example.com]
  - GitHub: [github.com/username2]
  - Website cá nhân: [gắn link vô]
- **[Tên thành viên 3]**
  - Email: [email3@example.com]
  - GitHub: [github.com/username3]
  - Website cá nhân: [gắn link vô]
- **[Tên thành viên 4]**
  - Email: [email4@example.com]
  - GitHub: [github.com/username4]
  - Website cá nhân: [gắn link vô]

## Kế hoạch dự kiến

Dự án được thực hiện trong 6 tuần với các mốc thời gian cụ thể như sau:

- **Tuần 1**:

  - Tải dataset FER-2013 từ Kaggle (https://www.kaggle.com/datasets/msambare/fer2013).
  - Tạo dữ liệu ánh sáng yếu (giảm độ sáng ngẫu nhiên 20-80%).
  - Viết đề cương NCKH (bao gồm phần đặt vấn đề, tổng quan tài liệu, phương pháp nghiên cứu).
  - **Song song**: Bắt đầu soạn thảo phần **Giới thiệu** và **Tổng quan tài liệu** của bài báo khoa học.
- **Tuần 2**:

  - Xây dựng và thử nghiệm thuật toán tăng cường dữ liệu thích ứng (adaptive data augmentation) dựa trên độ sáng của từng ảnh.
  - **Song song**: Tiếp tục viết phần **Phương pháp nghiên cứu** trong bài báo, mô tả thuật toán tăng cường dữ liệu.
- **Tuần 3**:

  - Huấn luyện mô hình MobileNetV3 cơ bản trên dữ liệu ánh sáng yếu (chưa tích hợp tăng cường thích ứng).
  - **Song song**: Viết phần **Thực nghiệm** (mô tả dataset, thiết kế thí nghiệm) và chuẩn bị phần **Kết quả** (để trống, điền sau).
- **Tuần 4**:

  - Tích hợp thuật toán tăng cường thích ứng vào mô hình, thực hiện fine-tuning MobileNetV3.
  - **Song song**: Cập nhật phần **Phương pháp nghiên cứu** (thêm chi tiết fine-tuning), viết phần **Kết luận** sơ bộ.
- **Tuần 5**:

  - Đánh giá mô hình (đo độ chính xác >70%, thời gian suy luận <0.1 giây/ảnh).
  - So sánh kết quả giữa mô hình cơ bản và mô hình với tăng cường thích ứng.
  - **Song song**: Điền kết quả vào phần **Kết quả**, viết phần **Thảo luận** (phân tích hiệu quả, hạn chế).
- **Tuần 6**:

  - Hoàn thiện code, kiểm tra lại toàn bộ hệ thống (đảm bảo chạy ổn định).
  - Hoàn thiện bài báo khoa học: chỉnh sửa định dạng, bổ sung hình ảnh minh họa (biểu đồ, kết quả).
  - Nộp báo cáo và chuẩn bị thuyết trình (nếu cần).

## Liên kết

- [schedule.xlsx](https://docs.google.com/spreadsheets/d/1fQEhZhOme_cUPzWFHYGgAEzErR-zbi63u4UeUeJ06Mo/edit?gid=0#gid=0) - File kế hoạch chi tiết (bao gồm timeline và phân bổ công việc).

## Phân bổ thời gian làm việc

- Mỗi thành viên dành ít nhất 3 giờ/tuần, tùy theo khối lượng công việc cụ thể.
- Họp nhóm 1-2 lần/tuần (trực tiếp hoặc online) để cập nhật tiến độ và giải quyết khó khăn.

### Công cụ hỗ trợ

- **GitHub**: Quản lý mã nguồn và tài liệu.
- **VSCode/Overleaf**: Viết và chỉnh sửa bài báo khoa học.
- **Microsoft Excel**: Tạo file `schedule.xlsx` để theo dõi tiến độ chi tiết.
