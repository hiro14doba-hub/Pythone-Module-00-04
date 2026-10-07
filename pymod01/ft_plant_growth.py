class Plant:
    name: str
    height: float
    old: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.old = self.old + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25.0
    plant1.old = 30

    plant1.show()
    start_height = plant1.height
    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    total_growth = round(plant1.height - start_height, 1)
    print("Growth this week: " + str(total_growth) + "cm")
