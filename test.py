def find_null_byte(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            if '\0' in line:
                print(f"Null byte found on line {i}")
        print(f"Null byte is not")

# Replace 'your_file.py' with your actual file path.
find_null_byte("C:\Program Files\Python311\Lib\importlib\__init__.py")

            


