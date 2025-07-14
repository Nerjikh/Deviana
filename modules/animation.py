import time

from test_main import client

class Animation:
    def __init__(self):
        self.frames = [
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "✨ Deviana is alive ✨"
        ]

    def run_intro(self):
        print("🎞️ Running Deviana's intro animation...")
        for frame in self.frames:
            print(frame)
            time.sleep(0.3)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Deviana AI — Your business empire"}