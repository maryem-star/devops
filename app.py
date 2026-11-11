"""Mini application pour le TP Git DevOps."""

APP_NAME = "devops-git-lab"


def hello(name="DevOps"):
    return f"Hello {name}"


def add(a, b):
    return a + b


def status():
    return {"app": APP_NAME, "status": "ok"}


if __name__ == "__main__":
    print(hello())
    print(status())
