from datetime import datetime
from pathlib import Path


def main() -> None:
    now = datetime.now()
    print("Ahoj, tu hello-automation!")
    print(f"Dnes je {now:%d.%m.%Y} a je {now:%H:%M:%S}")

    with Path("output.log").open("a", encoding="utf-8") as f:
        f.write(f"{now:%Y-%m-%d %H:%M:%S} - run OK\n")