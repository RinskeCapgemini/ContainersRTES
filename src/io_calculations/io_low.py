import time

def io_low(file_path):

    with open(file_path, 'w') as f:
        for i in range(1000):
            f.write(f"Line {i}: Hello World\n")
            f.flush()
            time.sleep(0.01)            # Delay to simulate low memory usage


if __name__ == "__main__":
    file_path = "/mnt/usb/test_io.txt"
    io_low(file_path)