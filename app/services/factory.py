from app.models.video import VideoPlatform
from app.strategies.base import DownloadStrategy
from app.strategies.youtube_strategy import YoutubeStrategy
from app.strategies.x_strategy import XStrategy 
from app.strategies.standar_strategy import StandardStrategy  


class StrategyFactory:

    @classmethod
    def get_strategy(cls, platform: VideoPlatform | None) -> DownloadStrategy:
        try:
            match platform:
                case VideoPlatform.YOUTUBE:
                    return YoutubeStrategy()
                case VideoPlatform.X:
                    return XStrategy()
                
                case _:
                    return StandardStrategy()
                
        except KeyError:
            raise ValueError(f"STRATEGIA NO IMPLEMENTADA PARA: {platform}")