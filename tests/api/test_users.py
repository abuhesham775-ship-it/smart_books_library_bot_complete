from schemas.user import UserRead


def test_user_schema():
    u = UserRead(id=1, points=0)
    assert u.id == 1
