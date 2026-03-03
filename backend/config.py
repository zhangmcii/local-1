import json
import os
import sys
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parent.parent
IS_FROZEN = bool(getattr(sys, 'frozen', False))
PROJECT_ROOT = Path(sys.executable).resolve().parent if IS_FROZEN else SOURCE_ROOT

def _load_video_folder_from_config():
    config_path = os.getenv('LOCAL_V_CONFIG_PATH')
    if not config_path or not os.path.exists(config_path):
        return None

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        folder = data.get('video_folder')
        if folder and os.path.isdir(folder):
            return folder
    except Exception:
        return None

    return None


# 视频文件夹路径（默认固定在代码中）
VIDEO_FOLDER_DEFAULT = r'E:\Downloads'

def reload_video_folder():
    global VIDEO_FOLDER
    configured = _load_video_folder_from_config()
    VIDEO_FOLDER = configured or VIDEO_FOLDER_DEFAULT

    # PyInstaller 场景兜底：如果目录不存在，尝试 exe 同目录下 public
    if IS_FROZEN and not os.path.exists(VIDEO_FOLDER):
        runtime_public = Path(sys.executable).resolve().parent / 'public'
        VIDEO_FOLDER = str(runtime_public)

    return VIDEO_FOLDER


VIDEO_FOLDER = reload_video_folder()

# 支持的视频格式
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.mkv', '.webm'}

# 默认分页大小
DEFAULT_PAGE_SIZE = 12
