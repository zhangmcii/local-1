import os
from pathlib import Path
from dotenv import load_dotenv

# 项目根目录
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_ROOT = Path(__file__).resolve().parent

# 优先读取 backend/.env，再读取项目根目录 .env
load_dotenv(BACKEND_ROOT / '.env')
load_dotenv(PROJECT_ROOT / '.env')

# 视频文件夹路径 - 从 .env 的 VIDEO_FOLDER 读取
VIDEO_FOLDER = os.getenv('VIDEO_FOLDER', str(PROJECT_ROOT / 'public'))
VIDEO_FOLDER = os.path.expanduser(VIDEO_FOLDER)

# 支持的视频格式
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.mkv', '.webm'}

# 默认分页大小
DEFAULT_PAGE_SIZE = 12
