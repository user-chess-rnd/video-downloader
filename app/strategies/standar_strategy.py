from app.strategies.base import DownloadStrategy


class StandardStrategy(DownloadStrategy):
    def ydl_opts(self, path: str, **_) -> dict:
        return {
            "format": "best",
            "noplaylist": True,
            "outtmpl": f"{path}/%(title)s.%(ext)s",
        }