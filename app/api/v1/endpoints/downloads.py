from fastapi import APIRouter
from app.services.downloader import VideoDownloader
from app.models.video import VideoInfo
from pydantic import BaseModel

router = APIRouter(
    prefix="/download"
)


@router.get("/")
async def get_info_video():
    return {"data": "VIDEO_DATA"}


class VideoRequest(BaseModel):
    url: str

@router.post("/")
def post_download_video(request: VideoRequest):

    if not request.url:
        return "ERROR SIN URL"

    vid_info = VideoInfo(url=request.url)
    descarga = VideoDownloader(vid_info).download(path="./downloads",only_sound=False)

    return {"descarga": descarga}
