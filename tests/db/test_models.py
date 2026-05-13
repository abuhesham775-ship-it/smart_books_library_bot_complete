from db.models import Base


def test_base_exists():
    assert Base is not None
