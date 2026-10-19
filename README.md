# Hệ thống quản lý khách sạn bằng Python

## 1. Giới thiệu

Đây là bài thi thực hành Python xây dựng hệ thống quản lý khách sạn trên giao diện dòng lệnh (CLI).

## 2. Chức năng

- Hiển thị danh sách phòng.
- Thêm phòng thường và phòng VIP.
- Đặt phòng và quản lý thông tin khách hàng.
- Trả phòng và thanh toán.
- Báo cáo tổng doanh thu và số phòng trống.
- Lưu và tải dữ liệu bằng file JSON.
- Xử lý lỗi nhập liệu và lỗi hệ thống.

## 3. Kiến thức áp dụng

- Lập trình hướng đối tượng (OOP).
- Kế thừa, đóng gói và đa hình.
- Chia module Python.
- Xử lý file JSON.
- Xử lý ngoại lệ (try-except).
- Danh sách, dictionary và vòng lặp.

## 4. Cấu trúc dự án

- `models.py`: Khai báo các lớp đối tượng.
- `services.py`: Xử lý nghiệp vụ quản lý khách sạn.
- `file_handler.py`: Lưu và đọc dữ liệu JSON.
- `main.py`: Giao diện menu CLI.
- `khachsan_data.json`: File dữ liệu được tạo khi lưu.

## 5. Cách chạy chương trình

Yêu cầu: Máy tính đã cài đặt Python 3.

Mở Terminal tại thư mục dự án và chạy:

```bash
py main.py
```
