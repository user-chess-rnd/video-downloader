from fastapi import APIRouter, HTTPException
from app.services.downloader import VideoDownloader
from app.models.video import VideoInfo
from pydantic import BaseModel

router = APIRouter(
    prefix="/download"
)


class VideoRequest(BaseModel):
    url: str

@router.get("/")
def get_info_video(url: str): 
    if not url:
        raise HTTPException(status_code=400, detail="URL es requerida")

    try:    
        vid_info = VideoInfo(url=url)
        data = VideoDownloader(vid_info).get_data_video()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"data": data}


@router.post("/")
def post_download_video(request: VideoRequest):
    if not request.url:
        raise HTTPException(status_code=400, detail="URL es requerida")

    try:
        vid_info = VideoInfo(url=request.url)
        descarga = VideoDownloader(vid_info).download(path="./downloads",only_sound=False)
        return {"descarga": descarga}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
