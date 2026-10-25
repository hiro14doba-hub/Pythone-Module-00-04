import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name = sys.argv[0]
    print(f"Program name: {program_name}")
    program_total = len(sys.argv)
    if program_total == 1:
        print("No arguments provided!")
    else:
        received_args = program_total - 1
        print(f"Arguments received: {received_args}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {program_total}")


if __name__ == "__main__":
    main()
