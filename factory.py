from video import VideoPlatform
from strategies.youtube_strategy import YoutubeStrategy
from strategies.base import DownloadStrategy

class StrategyFactory:
    _strategies = {
        VideoPlatform.YOUTUBE: YoutubeStrategy,
        # VideoPlatform.INSTAGRAM: InstagramStrategy,
        # VideoPlatform.TIKTOK: TiktokStrategy,
    }

    @classmethod
    def get_strategy(cls, platform: VideoPlatform) -> DownloadStrategy:
        try:
            return cls._strategies[platform]()
        except KeyError:
            raise ValueError(f"STRATEGIA NO IMPLEMENTADA PARA: {platform}")