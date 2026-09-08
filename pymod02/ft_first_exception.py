def input_temperature(temp_str: str)->int:
    return int(temp_str)

def test_temperature()->None:
    print("=== Garden Temperature ===")
    try:
        val = '25'
        print(f"Input data is '{val}'")
        res = input_temperature(val)
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
            val = 'abc'
            print(f"Input data is '{val}")
            res = input_temperature(val)
            print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")

def main()->None:
    test_temperature()

if __name__ == "__main__":
    main()

        