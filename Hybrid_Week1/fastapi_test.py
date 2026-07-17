from fastapi import FastAPI,UploadFile,File,Form
import uvicorn

app = FastAPI()
@app.post("/predict")
async def file_send(file:UploadFile = File(...),question:str = Form(...)):
    contents = await file.read()
    return {
        "status": "success",
        "filename": file.filename,
        "question_received": question,
        "fake_prediction": "Đây là kết quả giả lập"
    }

uvicorn.run(app,host="0.0.0.0",port=8000)