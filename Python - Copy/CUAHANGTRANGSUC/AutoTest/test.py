from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# Khởi tạo trình điều khiển Chrome
driver = webdriver.Chrome()

# Truy cập trang đăng nhập của Django Admin
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

# Tìm và nhập tên đăng nhập
inputUsername = driver.find_element(By.NAME, value="username")
print("Username input element found:", inputUsername)
inputUsername.send_keys("admin")
time.sleep(2.5)

# Tìm và nhập mật khẩu
password = driver.find_element(By.NAME, value="password")
print("Password input element found:", password)
password.send_keys("thereshzed")
time.sleep(2.5)

# Nhấn phím Enter để đăng nhập
password.send_keys(Keys.RETURN)

# Đợi 10 giây để xem kết quả
time.sleep(10)

# Đóng trình duyệt sau khi hoàn tất
driver.quit()
