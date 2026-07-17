import requests

# 1. Khai báo địa chỉ cái "Cổng" (API) mà bạn vừa mở bên FastAPI
url = "http://127.0.0.1:8000/predict"

# 2. Chuẩn bị "Gói hàng" (Gồm 1 file bất kỳ và 1 câu hỏi)
# Ở đây ta lấy tạm file quy_che.txt làm file mô phỏng thay cho ảnh
files = {'file': open(r"D:\CODING\RAG Test\quy_che.txt", 'rb')}
data = {'question': 'Trong file/ảnh này có thông tin gì?'}

print("Đang gửi yêu cầu từ máy Giám khảo đến máy của bạn...")

# 3. GỌI API! (Hành động ném gói hàng vào cổng)
response = requests.post(url, files=files, data=data)

# 4. In ra câu trả lời nhận được từ API của bạn
print("Kết quả trả về:")
print(response.json())
