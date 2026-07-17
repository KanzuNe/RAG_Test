from fastapi import FastAPI, File,Form, UploadFile
import uvicorn
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import io
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = key)
model = genai.GenerativeModel('gemini-3.1-flash-lite')



app = FastAPI()

@app.post("/predict")
async def get_image(file:UploadFile = File(...), question:str = Form(...)):
    image_bytes =await file.read()
    img = PIL.Image.open(io.BytesIO(image_bytes))
    response = model.generate_content(
        [question, img])
    return {"status": "success",
        "question_received": question,
        "fake_prediction": response.text
            }

uvicorn.run(app,host="0.0.0.0",port=8000)
