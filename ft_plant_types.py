#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, days: int, color: str
    ) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloom: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def blooming(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloom = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self.height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self):
        self.nutritional_value = self.nutritional_value + 1
        self.height = self.height + 2.1

    def age(self):
        self.days = self.days + 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.blooming()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
