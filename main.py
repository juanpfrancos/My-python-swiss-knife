from fastapi import FastAPI
from requests import get
from fastapi.responses import JSONResponse, Response
from scripts.create_xlsx import create_xlsx
from scripts.send_to_email import send_email
from scripts.get_images_flickr import get_photosets, get_urls
from config import API_COVID
import uvicorn

app = FastAPI(
    title="My python Swiss knife",
    description="Some scripts",
    version="1.0.0",
)


@app.get("/get_excel/", status_code=201)
async def excel():
    data = get(API_COVID).json()
    file_ = create_xlsx(data)
    return Response(content=file_, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@app.get("/send_attachment/", status_code=200)
async def send_attachment(email:str):
    data = get(API_COVID).json()
    file_ = create_xlsx(data)
    send_email(file_, email)


@app.get("/get_flickr_albums/", status_code=200)
async def flickr_albums():
    data = list(get_photosets())
    return JSONResponse(content=data)

@app.get("/get_flickr_album/", status_code=200)
async def get_flickr_album(id: str, photoset: str):
    data = list(get_urls(id))
    return JSONResponse(content=dict(photoset=data))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)