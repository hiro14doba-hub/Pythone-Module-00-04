def secure_archive(file_name: str,action: str, content: str)->tuple[bool,str]:
    try:
        if action == "read":
            with open(file_name,'r') as f:
                data = f.read()
                return (True,data)
        elif action == "write":
            with open(file_name,'w') as f:
                content = f.write(content)
                return (True,"Content successfully written to file")
    except Exception as e:
        return (False,str(e))

def main()->None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file","read",""))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd","read",""))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt","read",""))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("mk.txt","write","Mission complete!!!!"))

if __name__ == "__main__":
    main()
