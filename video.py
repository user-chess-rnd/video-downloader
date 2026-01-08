from urllib.parse import urlparse
from platform import VideoPlatform

class VideoInfo:
    def __init__(self, url: str, path: str):
        self.url = url
        self.download_path = path
        self.platform = detect_platform(url)

def detect_platform(url: str) -> VideoPlatform:
    domain = urlparse(url).netloc.lower()

    if "youtube" in domain or "youtu.be" in domain:
        return VideoPlatform.YOUTUBE
    if "instagram" in domain:
        return VideoPlatform.INSTAGRAM
    if "tiktok" in domain:
        return VideoPlatform.TIKTOK
    if "x.com" in domain:
        return VideoPlatform.X
    
    raise ValueError("Plataforma no soportada")



