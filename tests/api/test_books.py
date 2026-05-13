from api.main import app


def test_app_exists():
    assert app.title == "Smart Books Library Bot"
