import sys
from driver import Driver


def main():
    try:
        with open(sys.argv[1], "r") as f:
            raw_data = f.read().split('\n')
        data = Driver(raw_data)
        data.driving_summary()
    except IndexError:
        print("failure to read raw txt : pass file as first positional argument")


if __name__ == "__main__":
    main()