

from solutions.social import question_a #, tweets

mock_tweets = [
    {
        "id": 1,
        "full_text": "mock tweet text",
        "img_url": None,
        "user": {"screen_name": "mock_user1", "followers": 2},
        "likes_count": 150
    },
    {
        "id": 2,
        "full_text": "Mock tweet text 2",
        "img_url": None,
        "user": {"screen_name": "mockuser2", "followers": 4},
        "likes_count": 5
    }
]

def test_qa():
    #result = question_a(tweets)
    #assert result == "sandwhoa"

    result = question_a(mock_tweets)
    assert result == "mock_user1"
