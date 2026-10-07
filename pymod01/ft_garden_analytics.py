class Plant:
    class Status:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, {self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._status = self.Status()

    @staticmethod
    def check_years_old(age: int) -> bool:
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._status._show_count += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative ")
        else:
            self._age = new_age

    def grow(self) -> None:
        self._height = self._height + 2.1
        self._height = round(self._height, 1)
        self._status._grow_count += 1

    def age(self) -> None:
        self._age = self._age + 1
        self._status._age_count += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed (Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class Status(Plant.Status):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._produce_shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._status: Tree.Status = self.Status()

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )
        self._status._produce_shade_count += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value: float = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def display_statistics(plant: Plant) -> None:
    plant._status.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("--- Check year-old ---")
    print(f"Is 30 days more than a year? -> {Plant.check_years_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_years_old(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_statistics(anon)
