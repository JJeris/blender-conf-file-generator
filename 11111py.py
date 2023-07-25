import os

def is_symlink(folder_path):
    """Check if a folder is a symlink"""
    return os.path.islink(folder_path)

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder you want to check: ")

    if os.path.exists(folder_path):
        if is_symlink(folder_path):
            print(f"The folder '{folder_path}' is a symlink.")
        else:
            print(f"The folder '{folder_path}' is not a symlink.")
    else:
        print("The specified path does not exist.")
