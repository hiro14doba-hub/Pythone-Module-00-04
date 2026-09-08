import sys
from typing import IO
def main()->None:
    if len(sys.argv)!=2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    file: IO[str] | None = None
    content = ""
    try:
        file = open(file_name,'r')
        content = file.read()
        print(content,end="")
        file.close()
        print(f"File '{file_name}' closed.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}", file=sys.stderr)
        return
    
    print("Transform data:")
    lines = content.splitlines()
    trans_line = [line + "#" for line in lines]
    trans_content = "\n".join(trans_line)+"\n"
    print(trans_content,end="")
    print("Enter new file name (or empty): ",end="",flush=True)
    dest_name = sys.stdin.readline().strip()

    if not dest_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{dest_name}'")
    out_file: IO[str] | None = None
    try:
        out_file = open(dest_name,'w')
        out_file.write(trans_content)
        out_file.close()
        print(f"Data saved in file '{dest_name}'.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{dest_name}': {e}",file=sys.stderr)
        print("Data not saved.")
    


if __name__ == "__main__":
    main()