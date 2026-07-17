import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = key)
model = genai.GenerativeModel('gemini-3.1-flash-lite')

img = PIL.Image.open(r"D:\CODING\RAG Test\Hybrid_Week2\images.jpg")

response = model.generate_content(["Nói cho tôi biết xem đây là cái của nợ gì đi, trả về json gồm nội dung, nước nào, biển báo màu gì", img])
print(response.text)