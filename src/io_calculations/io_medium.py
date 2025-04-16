

def io_medium(file_path):
    
    data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 100

    with open(file_path, 'w') as f:
        for i in range(5000):
            f.write(f"Block {i}: {data}\n")
            f.flush()


if __name__ == "__main__":
    file_path = "/mnt/usb/test_io.txt"
    io_medium(file_path)