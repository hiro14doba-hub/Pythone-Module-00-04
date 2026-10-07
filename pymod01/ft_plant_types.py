class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

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

    def age(self) -> None:
        self._age = self._age + 1


class Flower(Plant):
    def __init__(
            self, name: str, height: float, age: int, color: str
    ) -> None:
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


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Plant")
    plant = Plant("Rose", 25.0, 30)
    plant.show()

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("=== Vegetable")
    veg = Vegetable("Tomato", 5.0, 10, "April")
    veg.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        veg.grow()
        veg.age()
    veg.show()
