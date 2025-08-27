import json
from bron_sdk_py.utils.http import HttpClient


MOCK_JWK = json.dumps({
    "kty": "EC",
    "crv": "P-256",
    "x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
    "y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
    "d": "870MB6gfuTJ4H3UnuUpxs5SwSxH2yf5K0uR49f6OzcP",
    "kid": "test-key-id",
})


def test_query_building(monkeypatch):
    captured = {}

    def fake_request(method, url, headers=None, data=None):
        captured["url"] = url
        captured["headers"] = headers
        class R:
            status_code = 200
            content = b"{}"
            def json(self):
                return {}
        return R()

    monkeypatch.setattr("requests.request", fake_request)

    http = HttpClient("https://api.bron.org", MOCK_JWK)
    http.request(method="GET", path="/api/v1/test", query={"limit": 10, "ids": [1,2,3]})

    assert "limit=10" in captured["url"]
    assert "ids=1%2C2%2C3" in captured["url"]
    assert captured["headers"]["Authorization"].startswith("ApiKey ")


