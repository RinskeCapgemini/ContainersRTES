import os
import random
import time


def io_heavy_random(file_path):
    # Create a large file to perform random writes
    with open(file_path, 'wb') as f:
        f.truncate(10 * 1024 * 1024)


    file_size = 10 * 1024 * 1024  # 10 GB file
    block_size = 4 * 1024  # 4 KB block (typical disk block size)

    with open(file_path, 'r+b') as f:
        for _ in range(10000):  # Perform 10,000 random writes
            offset = random.randint(0, file_size - block_size)
            f.seek(offset)
            f.write(os.urandom(block_size))
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":

    print("Starting I/O heavy random write test...")

    start_time = time.time()

    file_path = "/mnt/usb/test_io_random.txt"

    io_heavy_random(file_path)

    finish_time = time.time()
    duration = finish_time - start_time  # Calculate the duration

    print(f"Program runtime: {duration:.2f} seconds")