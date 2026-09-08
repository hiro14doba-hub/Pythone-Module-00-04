import sys
def main()->None:
    print("=== Command Quest ===")
    program_name = sys.argv[0]
    print(f"Program name: {program_name}")
    program_total = len(sys.argv)
    if program_total == 1:
        print("No arguments provided!")
    else:
        received_args = program_total - 1
        print(f"Arguments received: {received_args}")
        for i ,arg in enumerate(sys.argv[1:], start = 1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {program_total}")

if __name__ == "__main__":
    main()