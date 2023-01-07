# Thông tin nhóm
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

- Hệ điều hành: Windows 10, Windows 11
- Framework: Django, Bootstrap
- Database: SQL

# Hướng dẫn chạy project 

**1. Tạo một thư mục (folder) mà bạn muốn lưu project**

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

**4.Chuyển đến thư mục chứa project**
```
cd QuanLyHocSinh/QuanLyHocSinh
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

# Hướng dẫn deploy project lên Heroku
**1. Clone repo về máy cá nhân**
```
git clone <đường dẫn HTTPS của repo>
```
Sau đó cd vào repo vừa clone về

**2. Viết file requirements.txt**

Tạo file requirements.txt ở thư mục gốc của repo. Nội dung là tên các thư viện mà project cần sử dụng, và phiên bản của chúng nếu cần.

**3. Tạo file Procfile**

Tạo file Procfile ở thư mục gốc của repo để chỉ định cho heroku cách chạy project

**4. Chỉnh sửa settings.py**

- Thêm địa chỉ của heroku app, và localhost 127.0.0.1 vào ALLOWED_HOST
- Thêm đoạn code bên dưới vào cuối file:
```
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
```

**5. Update schema**

```
python manage.py migrate
```

**6. Tạo heroku app**
```python
heroku create <tên app>
```

**7. Kết nối heroku app với repo hiện tại**
```python
heroku git:remote -a <tên app>
```
**8. Commit các thay đổi lên git**
```
git add .
git commit -m "<messages>"
```
**9. Push git repo lên heroku**
```
git push heroku <tên branch muốn push>
```

# Link demo trên Youtube 


# Link web 


# Các chức năng đã hoàn thành
- Tiếp nhận học sinh
- Lập danh sách lớp
- Tra cứu học sinh
- Nhận bảng điểm môn
- Nhận báo cáo tổng kết
- Quản lí qui định

# Các chức năng cần làm thêm
- Xuất bảng điểm 
- Chỉnh sửa UI
