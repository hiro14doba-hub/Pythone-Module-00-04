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
        for i in range(1, program_total):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {program_total}")


if __name__ == "__main__":
    main()
