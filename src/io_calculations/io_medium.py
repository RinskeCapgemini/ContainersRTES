import sys

"""Medium calculations for I/O operations"""

def io_medium(file_path):
    # Write medium-sized blocks of data to the specified file.
    
    data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 100

    with open(file_path, 'w') as f:
        for i in range(5000):
            f.write(f"Block {i}: {data}\n")
            f.flush()


if __name__ == "__main__":

    test_type = sys.argv[0] 

    # Use command line argument to determine the test type
    if test_type == "native":
        file_path = r"\mnt\usb\test_io.txt" 
    elif test_type == "container":
        file_path = r"\app\usb\test_io.txt"
    
    io_medium(file_path)