#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def growth(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.days = self.days + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    rose.show()
    init_growth = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.growth()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - init_growth, 1)}cm")
