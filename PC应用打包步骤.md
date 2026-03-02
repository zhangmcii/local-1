# PC 应用打包步骤（前端 + 后端 exe 一体）

本项目使用 `Tauri + Vue + Flask`。目标是：
- 先把后端 `backend/app.py` 打成 `app.exe`
- 再把前端打包成桌面应用
- 应用启动时自动拉起后端 `app.exe`

## 1. 环境准备（Windows）

1. 安装 Node.js（建议 20+）
2. 安装 Python（建议 3.10+）
3. 安装 Rust（`rustup`）
4. 安装 Tauri 依赖（WebView2 / Visual Studio C++ Build Tools）
5. 安装 PyInstaller：

```bash
pip install pyinstaller
```

6. 安装前端依赖：

```bash
npm install
```

## 2. 配置视频目录

后端扫描目录写在：
- [`backend/config.py`](/Users/nizhenshi/Documents/proj/local_v/backend/config.py)

当前使用固定值 `VIDEO_FOLDER = r'E:\\Downloads'`。  
请改成你自己的视频目录（例如 `D:\\Videos`）。

## 3. 开发调试（自动启动后端 exe）

```bash
npm run tauri:dev:pc
```

这个命令会做两件事：
1. 先执行 `npm run backend:build`，生成 `src-tauri/resources/app.exe`
2. 再执行 `npm run tauri dev`，Tauri 启动时自动拉起 `app.exe`

## 4. 正式打包（生成安装包）

```bash
npm run tauri:build:pc
```

这个命令会做两件事：
1. 先生成最新后端 `app.exe` 到 `src-tauri/resources/`
2. 再执行 Tauri build，产出桌面安装包（`src-tauri/target/release/bundle/...`）

## 5. 关键脚本说明

`package.json` 新增脚本：
- `backend:build`：仅打包后端 exe
- `tauri:dev:pc`：开发模式一键启动（含后端）
- `tauri:build:pc`：发布模式一键打包（含后端）

## 6. 常见问题

1. `pyinstaller: command not found`
   - 先执行 `pip install pyinstaller`
   - 或用 `python -m PyInstaller` 方式替代

2. Tauri 报找不到 `app.exe`
   - 确认 `src-tauri/resources/app.exe` 已生成
   - 先单独运行 `npm run backend:build`

3. 应用打开但没有视频
   - 检查 `backend/config.py` 的 `VIDEO_FOLDER`
   - 检查目录下是否是支持的后缀：`.mp4/.mov/.mkv/.webm`
