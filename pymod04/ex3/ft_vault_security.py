def secure_archive(file_name: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, 'r') as f:
                data = f.read()
                return (True, data)
        elif action == "write":
            with open(file_name, 'w') as f:
                f.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: {action}")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read", ""))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("men.txt", "read", ""))

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read", ""))

    print("Using 'secure_archive' "
          "to write previous content to a new file:")
    print(secure_archive("secure_archive", "write", "Mission complete!!!!"))


if __name__ == "__main__":
    main()
