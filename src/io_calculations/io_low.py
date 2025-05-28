import sys

"""Light calculations for I/O operations"""	

def io_low(file_path):
    # Write Hello World to the specified file in a loop.

    with open(file_path, 'w') as f:
        for i in range(500):
            f.write(f"Line {i}: Hello World\n")
            f.flush()


if __name__ == "__main__":
    
    test_type = sys.argv[0]

    # Use command line argument to determine the test type
    if test_type == "native":
        file_path = r"\mnt\usb\test_io.txt" 
    elif test_type == "container":
        file_path = r"\app\usb\test_io.txt"
    
    io_low(file_path)