import os
import random


def io_heavy_random(file_path):
    file_size = 10 * 1024 * 1024 * 1024  # 10 GB file
    block_size = 4 * 1024  # 4 KB block (typical disk block size)

    with open(file_path, 'r+b') as f:
        for _ in range(1000000):  # Perform 1,000,000 random writes
            offset = random.randint(0, file_size - block_size)
            f.seek(offset)
            f.write(os.urandom(block_size))
            f.flush()
            os.fsync(f.fileno())


if __name__ == "__main__":
    file_path = "/mnt/usb/test_io_random.txt"

    # Create a large file to perform random writes
    with open(file_path, 'wb') as f:
        f.truncate(10 * 1024 * 1024 * 1024)  # Pre-allocate 10 GB file

    io_heavy_random(file_path)