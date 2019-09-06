import sys
from driver import Driver


def main():
    with open(sys.argv[1], "r") as f:
        raw_data = f.read().split('\n')
    x = Driver(raw_data)
    driving_summary = x.driving_summary()
    print(driving_summary)

if __name__ == "__main__":
    main()