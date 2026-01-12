from app.services.downloader import VideoDownloader
from app.models.video import VideoInfo

# PUNTO DE ENTRADA A LA API

url = ""
vid_info = VideoInfo(url=url)
VideoDownloader(vid_info).download(path="./downloads",only_sound=False)



