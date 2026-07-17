import requests
from openai.types.responses import response_file_search_tool_call_param

url = "http://127.0.0.1:8000/predict"

file = {'file':open(r"D:\CODING\RAG Test\Hybrid_Week2\images.jpg","rb")}
data = {'question':'đây là biển báo gì?'}

response = requests.post(url, files=file,data=data)

print("Đang gửi tới máy chủ")

print(response.json())