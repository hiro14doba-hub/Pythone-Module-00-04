class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def test_costome_error()->None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    errors = [PlantError("The tomato plant is wilting!"),WaterError("Not enough water in the tank!")]
    for err in errors:
        try :
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("All custome error types work correctly!")

def main()->None:
    test_costome_error()

if __name__ == "__main__":
    main()
