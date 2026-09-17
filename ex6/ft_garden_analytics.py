#!/usr/bin/env  python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def increment_grow(self) -> None:       
            self._grow_count += 1	

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:		
			self._show_count += 1

        def display(self, name: str):
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, {self._show_count} show")


    def __init__ (self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.stats = self.Stats()

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def year_older(days_old: int)-> bool:
        return days_old > 365

    def grow(self):
		self.height = self.height + 8.0
		self.stats.increment_grow()

    def age(self):
        self.days = self.days + 20
		self.stats.increment_age()

    def show(self)-> None:
        self.stats.increment_show()      
        print(f"{self.name}: {self.height}cm, {self.days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloom: bool = False

    def show(self)-> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloom:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloomed(self)-> None:
        self.bloom = True
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow()


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days, color)
		self.seeds: int = 0

	def bloomed(self) -> None:
		super().bloomed()
		self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self._shade_count} shade")

        def increment_shade(self) -> None:
            self._shade_count += 1
            
    def __init__(self, name: str, height: float, days: int, trunk_diameter: float)-> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter
        self.stats = self.Stats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    
    def produce_shade(self) -> None:
        self.stats.increment_shade()
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")

def display_stats(plant: Plant) -> None:
    plant.stats.display(plant.name)     

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.year_older(30)}")
    print(f"Is 400 days more than a year? -> {Plant.year_older(400)}")  
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    rose.bloomed()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.grow()
    sunflower.age()
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_stats(unknown)

