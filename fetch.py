"""读取JSON数据并打印字段。"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "videos.json"


def load_videos(path: Path = DATA_FILE) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def print_videos(videos: list[dict]) -> None:
    for video in videos:
        print(video["id"], video["title"], video["views"], video["likes"], video["comments"])


def main() -> None:
    videos = load_videos()
    print_videos(videos)
    print("共", len(videos), "条")


if __name__ == "__main__":
    main()