from app.models.video import VideoInfo
from app.services.factory import StrategyFactory
import os
import logging
import yt_dlp

logger = logging.getLogger(__name__)

class VideoDownloader:
    
    def __init__(self, video: VideoInfo):
        self.video = video
        self.strategy = StrategyFactory.get_strategy(video.platform)
    
    @staticmethod
    def ensure_path(path: str):
        os.makedirs(path, exist_ok=True)

    def get_data_video(self) -> dict:
        yt_opts = {}
        try:
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                info = ydl.extract_info(url=self.video.url, download=False)

        except Exception as e:
            raise TypeError(f"Error al obtener datos del video: {e}")
        
        return ydl.sanitize_info(info)
    
    def download(self, path: str, only_sound=False, extra_parameters=None) -> str:
        """
        Ejecuta la descarga del video configurado.
        """
        self.ensure_path(path)
        logger.info(f"Iniciando descarga para: {self.video.url} en {path}")

        opts = self.strategy.ydl_opts(
            extra_parameters=extra_parameters,
            only_sound=only_sound,
            path=path
        )

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([self.video.url])
            logger.info(f"Descarga completada exitosamente: {self.video.url}")

        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Error de descarga de yt-dlp: {e}", exc_info=True)
            raise RuntimeError(f"Error en la descarga: {e}") from e
        except Exception as e:
            logger.critical(f"Error inesperado durante la descarga: {e}", exc_info=True)
            raise RuntimeError(f"Error crítico del sistema: {e}") from e

        return path
