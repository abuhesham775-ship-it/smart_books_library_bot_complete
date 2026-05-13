from schemas.point import PointTransactionRead


def test_points_schema():
    p = PointTransactionRead(id=1, user_id=1, points=10, reason="read")
    assert p.points == 10
