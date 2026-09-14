"""整合演示：读取数据 → 分析评分 → 写入数据库 → 从数据库读回报告。"""

import database
import fetch
from user_manager import UserManager
from video_analyzer import analyze_video


def main() -> None:
    # 1. 准备数据库：建立连接并建表
    conn = database.init_db()

    # 2. 用户模块：创建两个用户，写进 users 表
    manager = UserManager()
    manager.add_user("张三", "zhangsan@example.com")
    manager.add_user("李四", "lisi@example.com")
    users = manager.list_users()
    for user in users:
        database.insert_user(conn, user)
    print("用户已入库：", len(users), "人")

    # 3. 读取视频数据（来自 data/videos.json）
    videos = fetch.load_videos()
    print("读取到视频：", len(videos), "条")

    # 4. 逐条分析，并把视频和分析报告写进数据库
    for video in videos:
        video_id = database.insert_video(conn, video)
        report = analyze_video(video)
        database.insert_report(conn, video_id, report)

    # 5. 从数据库读回：报告 JOIN 视频
    rows = database.list_reports_with_video(conn)
    print("数据库里的视频报告：")
    for row in rows:
        print(row["title"], row["views"], row["score"], row["level"])

    conn.close()


if __name__ == "__main__":
    main()