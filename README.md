# Thành viên nhóm
| MSSV | Họ và Tên |
| :---: | :---: |
| 20120037 | Trần Thị Minh Anh | 
| 20120042 | Trương Quân Bảo | 
| 20120046 | Ngô Xuân Chiến |
| 20120146 | Nguyễn Thị Châu Ngọc |
| 20120165 | Hồng Nhất Phương |

# Giới thiệu project: Quản lý học sinh
- Chúng ta đang thực hiện chuyển đổi số, việc áp dụng công nghệ thông tin vào những công việc quản lý sẽ giúp ích rất nhiều.Đó là lí do nhóm xây dựng lên hệ thống quản lí học sinh
-  Hệ thống giúp ta quản lí  dữ liệu  an toàn, tổ chức, sắp xếp dữ liệu một cách khoa học để tránh phải làm những công việc lặp đi lặp lại.

# Môi trường thực thi

- Hệ điều hành: Windows
- Framework: Django, Bootstrap
- Database: SQL

# Hướng dẫn chạy project 

**1. Tạo một thư mục (folder) để lưu project**

**2. Tạo một môi trường trên máy và kích hoạt môi trường**

**Cài đặt môi trường**
```
pip install virtualenv
```

**Tạo môi trường**

```
python -m venv venv
```

**Kích hoạt môi trường**

```
venv/scripts/activate
```

**3. Clone project**
```
git clone https://github.com/ngoxuanchien/QuanLyHocSinh.git
```

**4. Chuyển đến thư mục chứa project**
```
cd QuanLyHocSinh
```

**5. Cài đặt các thư viện từ 'requirements.txt'**
```python
pip install -r requirements.txt
```

**6. Database migration**
```python
python manage.py migrate
```

**7. Tạo tài khoản Admin (Super User)**
```python
python manage.py createsuperuser
``` 

**8. Chạy chương trình**
```python
python manage.py runserver
```

**9. Đăng nhập và sử dụng**



# Link demo trên Youtube 


# Current status
- Đăng nhập bằng tài khoản admin
- Thêm, xóa học sinh
- Chỉnh sửa thông tin học sinh
- Lập danh sách lớp
- Xem danh sách lớp
- Tra cứu học sinh
- Nhận bảng điểm môn
- Xem báo cáo tổng kết
- Quản lý quy định

# Future works
- Chỉnh sửa giao diện người dùng
- Thêm chức năng tạo tài khoản
