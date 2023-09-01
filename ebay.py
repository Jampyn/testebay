from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from datetime import datetime

# สร้าง instance ของเบราว์เซอร์
driver = webdriver.Chrome()  # ต้องมี Chrome WebDriver ใน PATH

# เปิดหน้าเว็บ eBay
driver.get("https://www.ebay.com")

# ขยายหน้าต่างเบราว์เซอร์ให้เต็มจอ
driver.maximize_window()

# ค้นหาคำว่า "psp" ในช่องค้นหา
search_box = driver.find_element("name", "_nkw")
search_box.send_keys("psp")
search_box.send_keys(Keys.RETURN)

# รอให้ผลการค้นหาปรากฏขึ้น
driver.implicitly_wait(10)  # รอไม่เกิน 10 วินาที

# เก็บเนื้อหาของหน้าเว็บ
page_content = driver.page_source

# ตรวจสอบการผ่านหรือไม่ผ่าน
if "psp" in page_content:
    result = "pass"
    reason = "Test passed successfully."
else:
    result = "failed"
    reason = "Test failed. Keyword 'psp' not found in page content."

# เพิ่มข้อมูลลงในไฟล์ CSV
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
csv_row = [timestamp, result, reason]

with open("test_history.csv", "a", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_row)


