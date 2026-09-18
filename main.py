"""FastAPI 服务入口：今天先提供一个 /videos 接口。"""

from fastapi import FastAPI

from fetch import load_videos

app = FastAPI(title="AI-Video-Analyzer API")


@app.get("/videos")
def get_videos() -> list[dict]:
    """返回 data/videos.json 里的全部视频。"""
    return load_videos()
