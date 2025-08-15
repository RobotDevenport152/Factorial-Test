import os

class DemoFile:

    def __init__(self, filename: str):
        self.filename = filename

    def write_file(self, text: str) -> None:
        """Write text to the file, overwriting existing content."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(text)

    def read_file(self) -> str:
        """Read and return the entire content of the file."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()


def main():
    # Define the full path to your file
    file_path = os.path.join(
        r"C:\Users\Ben\Desktop\Yoobee Courses\MSE 800 Professional Software Engineering(Programming Languages)\Week 3",
        "demo_file_activity1.txt"
    )

    demo_file = DemoFile(file_path)

    print("=== Reading initial content ===")
    try:
        print(demo_file.read_file())
    except FileNotFoundError:
        print("[INFO] File not found. It will be created when writing.")

    print("\n=== Writing 'Hello World' to file ===")
    demo_file.write_file('Hello World')

    print("\n=== Reading updated content ===")
    print(demo_file.read_file())


if __name__ == "__main__":
    main()
