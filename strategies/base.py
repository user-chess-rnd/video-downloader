from abc import ABC, abstractmethod

class DownloadStrategy(ABC):

    @abstractmethod
    def ydl_opts(
        self,
        path: str,
        only_sound = False,
        extra_parameters: set[str] | None = None,
    ) -> dict:
        pass