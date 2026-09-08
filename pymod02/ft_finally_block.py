class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

def water_plant(plant_name: str)->None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")

def test_watering_system()->None:
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        valid_plants = ["Tomato", "Lettuce", "Carrots"]
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        invalid_plants = ["Tomato", "lettuce", "Carrots"]
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

def main()->None:
    print("=== Garden Watering System ===")
    test_watering_system()
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    main()

        