#!/usr/bin/env  python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_count: int = 0
            self.age_count: int = 0
            self.show_count: int = 0

        def display(self, name: str):
            print(f"[statistics for {name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")


    def __init__ (self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.stats = self.Stats()

    @staticmethod
    def year_older(days_old: int)-> None:
        days_old:int = days_old
        print(f"Is {days_old} days more than a year? -> {days_old>365}")

    def show(self)-> None:
        self.stats.show_count += 1        
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom: bool = False

    def show(self)-> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom == False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully")

    def bloomed(self)-> None:
        self.bloom = True
        print(f"[asking the rose to grow and bloom]")
        self.stats.grow_count += 1


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_count: int = 0

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self.shade_count} shade")
            
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float)
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self.stats = self.Stats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats.shade_count += 1
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
        

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.year_older(30)
    Plant.year_older(400)
    print("")
    print("=== Flower")
    rose = Flower("Rose", 23.0, 10, "red")
    rose.show()
    rose.stats.display(rose.name)
    rose.bloomed()
    rose.show()
    rose.stats.display(rose.name)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)

    
    