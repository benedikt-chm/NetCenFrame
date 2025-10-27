"""Configuration for NetCenFrame"""
from dataclasses import dataclass
# from functools import cache

@dataclass
class _Config:
    """
    configuration object for the NetCenFrame library.
    """

    relativize: bool = True
    parallel_active: bool = True
    n_jobs: int = 3
    sort: bool = True

#
# @cache
# def config():
#     """make sure configuring works by returning an object"""
#     config_ = Config()
#     # config_ = Config(Targets=targets,
#     #                  FFmpeg=ffmpeg_config,
#     #                  Whisper=whisper_config,
#     #                  Translate=translate_config,
#     #                  Srt=srt_config,
#     #                  Log=log_config)
#     return config
#

def _init_config():
    config = _Config()
    return config

# Public name: the configuration instance already loaded.
# Other code can use and import `Config` alone:
Config = _init_config()
