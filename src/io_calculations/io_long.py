import os
import sys

"""Heavy calculations for I/O operations"""

def io_long(file_path):
    # Write large blocks of random data to the specified file.

    data = os.urandom(1 * 1024 * 1024) # 1 MB of random data 

    with open(file_path, 'wb') as f:
        for i in range(1000):
            f.write(data)
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":
    test_type = sys.argv[0]

    # Use command line argument to determine the test type
    if test_type == "native":
        file_path = r"\mnt\usb\test_io.txt" 
    elif test_type == "container":
        file_path = r"\app\usb\test_io.txt"

    io_long(file_path)


