"""视频分析模块：根据互动数据计算基础评分与等级。"""

from fetch import load_videos

BURST_THRESHOLD = 10.0
NORMAL_THRESHOLD = 3.0


def compute_score(views: int, likes: int, comments: int) -> float:
    """点赞率与评论率各占一半，得分＝(likes/views + comments/views) × 100。"""
    safe_views = max(views, 1)
    return round((likes / safe_views + comments / safe_views) * 100, 2)


def analyze_video(video: dict) -> dict:
    """计算单个视频的得分和等级：10以上爆款，3以上一般，其余待优化。"""
    score = compute_score(video["views"], video["likes"], video["comments"])
    if score >= BURST_THRESHOLD:
        level = "爆款"
    elif score >= NORMAL_THRESHOLD:
        level = "一般"
    else:
        level = "待优化"
    return {
        "id": video["id"],
        "title": video["title"],
        "score": score,
        "level": level,
    }


def analyze_all(videos: list[dict]) -> list[dict]:
    """批量分析视频，返回每个视频的得分和等级。"""
    return [analyze_video(video) for video in videos]


def main() -> None:
    for result in analyze_all(load_videos()):
        print(result["id"], result["title"], result["score"], result["level"])


if __name__ == "__main__":
    main()
