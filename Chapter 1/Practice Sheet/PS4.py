import os

def print_directory_contents(path):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for i in entries:
                print(i.name)
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{path}'.")

if __name__ == "__main__":
    # Example usage
    directory_path = input("Enter the directory path: ")
    print_directory_contents(directory_path)
