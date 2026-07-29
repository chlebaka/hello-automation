from datetime import datetime


def main() -> None:
    now = datetime.now()
    print("Ahoj, tu hello-automation!")
    print(f"Dnes je {now:%d.%m.%Y} a je {now:%H:%M:%S}")


if __name__ == "__main__":
    main()