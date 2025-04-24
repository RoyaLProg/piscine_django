import sys


def getStatesAndCapitals():
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
    return [states, capital_cities]


def getCity(key):
    [states, capital_cities] = getStatesAndCapitals()

    return capital_cities.get(states.get(key))


def getState(value):
    [states, capital_cities] = getStatesAndCapitals()

    return (list(states.keys())[list(states.values()).index(list(capital_cities.keys())[list(capital_cities.values()).index(value)])])


def capitalize(value):
    words = value.split(" ")
    new = []
    for w in words:
        new.append(w.capitalize())

    return " ".join(new)


def main():
    argv = sys.argv[1:]
    if len(argv) != 1:
        return
    [states, capital_cities] = getStatesAndCapitals()

    to_find = argv[0].split(",")

    for v in to_find:
        v = v.strip()
        if len(v) == 0:
            continue
        name = capitalize(v)
        if name in capital_cities.values():
            print(f"{name} is the capital of {getState(name)}")
        elif name in states.keys():
            print(f"{getCity(name)} is the capital of {name}")
        else:
            print(f"{v} is neither a capital city nor a state")


if __name__ == "__main__":
    main()
