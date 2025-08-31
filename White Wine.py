import pandas as pd

class DemoFile:
    def __init__(self, filename):
        self.filename = filename

    def calculate(self):
        reader = pd.read_csv(self.filename, sep=';')
        print(f"maximum: {reader['alcohol'].max():.2f}")
        print(f"minimum: {reader['alcohol'].min():.2f}")
        print(f"average: {reader['alcohol'].mean():.2f}")
        print("==================")
        print(f"average of absolute values: {reader['alcohol'].abs().mean():.2f}")

def main():
    demoFile = DemoFile(r"C:\Users\Ben\Desktop\Test\White Wine.csv")
    demoFile.calculate()

if __name__ == "__main__":
    main()
