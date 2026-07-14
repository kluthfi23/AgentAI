from app.version import APP_NAME, VERSION


class AgentAI:

    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION

    def start(self):
        print("=" * 40)
        print(f"{self.name}")
        print(f"Version : {self.version}")
        print("Status  : Ready")
        print("=" * 40)
