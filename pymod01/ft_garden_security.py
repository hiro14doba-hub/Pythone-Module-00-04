class Plant:
    def __init__(self,name: str, height: float, age: int)->None:
        self._name = name
        self._height = height
        self._age = age

    def show(self)->None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_height(self)->float:
        return self._height

    def get_age(self)->int:
        return self._age

    def set_height(self,new_height: float)->None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = new_height

    def set_age(self,new_age:int)->None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative ")
        else:
            self._age = new_age

if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant1 = Plant("Rose",15.0,10)
    print("Plant created: " , end="")
    plant1.show()

    plant1.set_height(25.0)
    print("Height updated: 25cm")
    plant1.set_age(30)
    print("Age updated: 30 days")

    plant1.set_height(-5.0)
    print("Height update rejected")
    plant1.set_age(-10)
    print("Age update rejected")

    print("Current state: ", end="")
    plant1.show()
