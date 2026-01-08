from strategies.base import DownloadStrategy


class YoutubeStrategy(DownloadStrategy):
    def ydl_opts(self, path, only_sound=False, extra_parameters = None):

        extra_parameters = extra_parameters or set()
        is_not_playlist = "playlist" not in extra_parameters

        format_download = (
            "m4a/bestaudio/best"
            if only_sound
            else "bestvideo+bestaudio/best"
        )

        options = {
            'format': format_download,
            'noplaylist': is_not_playlist,
            'outtmpl': f'{path}/%(title)s.%(ext)s',
        }

        if only_sound:
            options["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }]

        return options

