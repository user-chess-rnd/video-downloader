from video import VideoInfo
from factory import StrategyFactory
import os
import yt_dlp

class VideoDownloader:
    
    def __init__(self, video: VideoInfo):
        self.video = video
        self.strategy = StrategyFactory.get_strategy(video.platform)
    
    @staticmethod
    def ensure_path(path: str):
        os.makedirs(path, exist_ok=True)
    
    def download(self, path=None, only_sound=False, extra_parameters=None):

        path = path or self.video.download_path
        self.ensure_path(path)

        opts = self.strategy.ydl_opts(
            extra_parameters=extra_parameters,
            only_sound=only_sound,
            path= path
        )

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([self.video.url])

        except Exception as e:
            raise RuntimeError(f"Error en la descarga: {e}") from e



