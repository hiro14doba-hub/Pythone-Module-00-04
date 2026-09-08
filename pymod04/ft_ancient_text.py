import sys
import typing
from typing import IO
def main()->None:
    if len(sys.argv)!=2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    print(f"---","\n")

    file: IO[str] | None = None
    content = ""
    try:
        file = open(file_name,'r')
        content = file.read()
        print(content)
        file.close()
        print("---")
        print(f"File '{file_name}' closed.")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
        return

if __name__ == "__main__":
    main()
    