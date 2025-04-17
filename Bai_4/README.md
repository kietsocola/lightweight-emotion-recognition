# Nhận diện biểu cảm khuôn mặt trong điều kiện ánh sáng yếu sử dụng CNN nhẹ kết hợp kỹ thuật tăng cường dữ liệu thích ứng

## Giới thiệu

Dự án này tập trung vào việc phát triển một mô hình nhận diện biểu cảm khuôn mặt (Facial Expression Recognition - FER) trong điều kiện ánh sáng yếu, một thách thức thực tế trong các ứng dụng như giám sát an ninh, giao tiếp người-máy, và phân tích cảm xúc trong môi trường không lý tưởng. Để giải quyết vấn đề này, chúng tôi sử dụng một mạng nơ-ron tích chập (CNN) nhẹ (lightweight CNN) dựa trên kiến trúc MobileNetV3, kết hợp với kỹ thuật **tăng cường dữ liệu thích ứng (adaptive data augmentation)** để cải thiện hiệu suất mô hình trên các ảnh có ánh sáng yếu.

### Mục tiêu nghiên cứu

- Xây dựng một mô hình CNN nhẹ để nhận diện 7 biểu cảm cơ bản (vui, buồn, tức giận, sợ hãi, ngạc nhiên, ghê tởm, trung tính) trong điều kiện ánh sáng yếu.
- Phát triển thuật toán tăng cường dữ liệu thích ứng, tự động điều chỉnh các phép biến đổi (như gamma correction, contrast stretching) dựa trên mức độ sáng của từng ảnh.
- Đánh giá hiệu quả của mô hình so với các phương pháp cơ bản không sử dụng tăng cường thích ứng, hướng tới độ chính xác cao (>70%) và tốc độ suy luận nhanh (<0.1 giây/ảnh trên CPU).

### Ý nghĩa khoa học và thực tiễn

- **Khoa học**: Góp phần vào nghiên cứu cải tiến CNN cho bài toán FER trong điều kiện ánh sáng khó, đặc biệt với kỹ thuật tăng cường dữ liệu thích ứng – một hướng ít được khai thác trong 5 năm gần đây (2020-2025).
- **Thực tiễn**: Ứng dụng tiềm năng trong các hệ thống camera giám sát ban đêm, phân tích cảm xúc tự động, và thiết bị nhúng có tài nguyên hạn chế.

## Tính mới

Trong giai đoạn 2020-2025, mặc dù nhận diện biểu cảm khuôn mặt đã đạt nhiều tiến bộ với các mô hình CNN như ResNet và EfficientNet, các nghiên cứu chủ yếu tập trung vào điều kiện ánh sáng bình thường. Các phương pháp xử lý ánh sáng yếu thường sử dụng GAN hoặc Retinex, nhưng phức tạp và không tối ưu cho thời gian ngắn. Đề tài này mang lại tính mới bằng cách:

- Sử dụng CNN nhẹ (MobileNetV3) để cân bằng giữa độ chính xác và tốc độ.
- Đề xuất thuật toán tăng cường dữ liệu thích ứng, phân tích mức độ sáng của từng ảnh để áp dụng các biến đổi phù hợp, thay vì sử dụng tăng cường cố định như các nghiên cứu trước.

## Dataset

- **Tên dataset**: FER-2013
- **Nguồn**: https://www.kaggle.com/datasets/msambare/fer2013
- **Mô tả**: Bộ dữ liệu chứa khoảng 35.000 ảnh khuôn mặt đen trắng (48x48 pixel) với 7 biểu cảm (angry, disgust, fear, happy, sad, surprise, neutral).
- **Cách sử dụng**:
  - Tạo điều kiện ánh sáng yếu bằng cách giảm độ sáng ngẫu nhiên (20-80%).
  - Áp dụng thuật toán tăng cường dữ liệu thích ứng để cải thiện chất lượng ảnh trước khi huấn luyện.

## Phương pháp nghiên cứu

1. **Tiền xử lý dữ liệu**:
   - Tạo ảnh ánh sáng yếu từ FER-2013.
   - Xây dựng thuật toán tăng cường dữ liệu thích ứng dựa trên độ sáng trung bình hoặc histogram của từng ảnh.
2. **Mô hình CNN**:
   - Sử dụng MobileNetV3 pre-trained, fine-tuning trên dữ liệu ánh sáng yếu.
   - Kết hợp nhánh xử lý đặc trưng từ ảnh đã tăng cường.
3. **Đánh giá**:
   - So sánh hiệu suất giữa mô hình cơ bản (chỉ dùng RGB) và mô hình với tăng cường thích ứng.
   - Đo độ chính xác và thời gian suy luận trên tập test.

## Cấu trúc dự án

- `data/`: Thư mục chứa dataset FER-2013 và ảnh đã tăng cường.
- `src/`: Thư mục chứa mã nguồn:
  - `preprocess.py`: Script tiền xử lý dữ liệu và tạo ánh sáng yếu.
  - `augmentation.py`: Script xây dựng thuật toán tăng cường dữ liệu thích ứng.
  - `train.py`: Script huấn luyện mô hình CNN.
  - `evaluate.py`: Script đánh giá mô hình.
- `models/`: Thư mục lưu mô hình đã huấn luyện.
- `README.md`: File này (tổng quan dự án).
- `SCHEDULE.md`: File kế hoạch dự án
- `report/`: Thư mục chứa bài báo khoa học (sau khi hoàn thành).

## Lịch trình thực hiện (6 tuần)

- **Tuần 1**: Tải dataset, tạo dữ liệu ánh sáng yếu, viết đề cương.
- **Tuần 2**: Xây dựng và thử nghiệm thuật toán tăng cường dữ liệu thích ứng.
- **Tuần 3**: Huấn luyện MobileNetV3 cơ bản trên dữ liệu.
- **Tuần 4**: Tích hợp tăng cường thích ứng, fine-tuning mô hình.
- **Tuần 5**: Đánh giá mô hình, so sánh kết quả.
- **Tuần 6**: Hoàn thiện code, viết bài báo khoa học.

## Yêu cầu hệ thống

- **Phần mềm**: Python 3.8+, TensorFlow/Keras, OpenCV, NumPy.
- **Phần cứng**: CPU (tối thiểu 8GB RAM), GPU (nếu có) để tăng tốc huấn luyện.

## Hướng dẫn cài đặt

1. Clone repository:
   ```bash
   git clone https://github.com/ten-du-an-cua-ban.git
   cd ten-du-an-cua-ban
   ```
