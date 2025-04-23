import sys


def getCity(key):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if key not in states.keys():
        print("Unknow Country")

    else:
        print(f"{capital_cities.get(states.get(key))}")


def main():
    argv = sys.argv[1:]
    if len(argv) != 1:
        return

    getCity(argv[0])


if __name__ == "__main__":
    main()
