from urllib.parse import urlparse
from enum import Enum

class VideoPlatform(Enum):
    YOUTUBE = "youtube"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    X = "x"
    OTHER = "other"


class VideoInfo:
    def __init__(self, url: str):
        self.url = url
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
    
    try:
        return VideoPlatform.OTHER
    except:
        raise ValueError("Plataforma no soportada")



