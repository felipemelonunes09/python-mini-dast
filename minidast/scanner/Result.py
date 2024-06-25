
class Result():

    def __init__(self, description: str, url: str, risk: str) -> None:
        self.description = description
        self.url = url
        self.risk = risk

    def to_dict(self) -> dict:
        return {
            "url":         self.url,
            "risk":        self.risk,
            "description": self.description
        }
