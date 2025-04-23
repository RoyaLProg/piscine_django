import sys


def getState(value):
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

    if value not in capital_cities.values():
        print("Unknow capital city")

    else:
        print(list(states.keys())[list(states.values()).index(list(capital_cities.keys())[list(capital_cities.values()).index(value)])])


def main():
    argv = sys.argv[1:]
    if len(argv) != 1:
        return

    getState(argv[0])


if __name__ == "__main__":
    main()
