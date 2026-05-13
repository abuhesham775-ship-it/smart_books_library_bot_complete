from schemas.recommendation import RecommendationRead


def test_reco_schema():
    r = RecommendationRead(id=1, user_id=1, book_id=1, score=0.9)
    assert r.score > 0
