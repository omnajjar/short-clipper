from fastapi import FastAPI, Form
from service import process_video

app = FastAPI()


@app.post("/process_video")
async def process_video_endpoint(video_url: str = Form(...), email: str = Form(...)):
    response_data = process_video(video_url, email)
    return response_data


@app.get("/")
async def get_version():
    return {"version": "0.0.1"}
