import os
import time

def io_long(file_path):

    block = os.urandom(1 * 1024 * 1024) # 1 MB of random data 

    with open(file_path, 'wb') as f:
        for i in range(1000):
            f.write(block)
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":

    file_path = "/mnt/usb/test_io.txt"
    io_long(file_path)


