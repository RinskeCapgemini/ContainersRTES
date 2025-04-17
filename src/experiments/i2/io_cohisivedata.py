import shutil

def copy_binary_file(source_path, destination_path):
    """
    Copies a binary file from the source path to the destination path.

    Args:
        source_path (str): Path to the source binary file.
        destination_path (str): Path to the destination where the file will be written.
    """
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"Binary file copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying file: {e}")


if __name__ == "__main__":
    # Path to the existing binary file
    source_file = "/path/to/your/source_file.bin"  # Replace with the path to your binary file

    # Path to the destination (e.g., USB stick)
    destination_file = "/mnt/usb/test_1gb.bin"  # Adjust this path as needed

    # Copy the binary file
    copy_binary_file(source_file, destination_file)