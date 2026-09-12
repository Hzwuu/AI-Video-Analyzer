"""用户管理模块：只做纯逻辑，不涉及数据库和界面。"""


class UserNotFoundError(Exception):
    """按ID查不到用户时抛出。"""


class DuplicateUserError(Exception):
    """用户名或邮箱重复时抛出。"""


class UserManager:
    """在内存里管理用户，作为最小可运行的业务模块。"""

    def __init__(self) -> None:
        self._users: dict[int, dict[str, str]] = {}
        self._next_id: int = 1

    def add_user(self, username: str, email: str) -> int:
        """新增用户并返回分配的用户ID。"""
        if not username or not email:
            raise ValueError("用户名和邮箱不能为空")
        for user in self._users.values():
            if user["username"] == username:
                raise DuplicateUserError(f"用户名已存在：{username}")
            if user["email"] == email:
                raise DuplicateUserError(f"邮箱已存在：{email}")
        user_id = self._next_id
        self._users[user_id] = {"username": username, "email": email}
        self._next_id += 1
        return user_id

    def get_user(self, user_id: int) -> dict[str, str]:
        """按ID查询用户，查不到就抛异常。"""
        if user_id not in self._users:
            raise UserNotFoundError(f"用户不存在：{user_id}")
        return dict(self._users[user_id])

    def list_users(self) -> list[dict[str, str]]:
        """按ID升序返回所有用户。"""
        return [dict(self._users[uid]) for uid in sorted(self._users)]