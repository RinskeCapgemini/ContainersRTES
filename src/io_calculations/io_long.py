import os
import time

def io_long(file_path):

    block = os.urandom(1 * 1024 * 1024)

    with open(file_path, 'wb') as f:
        for i in range(1000):
            f.write(block)
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":

    start_time = time.time()

    print(f"Starting time is {start_time:.2f} seconds")

    file_path = "/mnt/usb/test_io.txt"
    io_long(file_path)


    finish_time = time.time() - start_time

    print(f"Time taken: {finish_time:.2f} seconds")