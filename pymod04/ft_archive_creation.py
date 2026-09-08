import sys
from typing import IO
def main()->None:
    if len(sys.argv)!=2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
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
    
    print("\n","Transform data:")
    print(f"---","\n")
    lines = content.splitlines()
    trans_line = [line + "#" for line in lines]
    trans_content = "\n".join(trans_line)+"\n"
    print(trans_content,end="")
    dest_name = input("Enter new file name (or empty): ")

    if not dest_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{dest_name}'")
    out_file: IO[str] | None = None
    try:
        out_file = open(dest_name,'w')
        out_file.write(trans_content)
        out_file.close()
        print("Data saved in file 'new_fragment.txt'.")
    except Exception as e:
        print(f"Error saving file '{dest_name}': {e}")
    


if __name__ == "__main__":
    main()