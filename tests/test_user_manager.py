"""user_manager 的单元测试。"""

import pytest

from user_manager import DuplicateUserError, UserManager, UserNotFoundError


def test_add_user_returns_id() -> None:
    """新增用户后应该拿到一个用户ID。"""
    manager = UserManager()
    user_id = manager.add_user("张三", "zhangsan@example.com")
    assert user_id == 1


def test_duplicate_username_raises() -> None:
    """重复的用户名应该报错。"""
    manager = UserManager()
    manager.add_user("张三", "zhangsan@example.com")

    with pytest.raises(DuplicateUserError):
        manager.add_user("张三", "zhangsan2@example.com")


def test_get_missing_user_raises() -> None:
    """查询不存在的用户应该报错。"""
    manager = UserManager()

    with pytest.raises(UserNotFoundError):
        manager.get_user(999)
