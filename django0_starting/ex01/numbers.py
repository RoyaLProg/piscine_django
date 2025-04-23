def main():
    file = open("./numbers.txt")
    numbers = file.read().split(',')
    file.close()
    for x in numbers:
        if len(x):
            print(x)


if __name__ == "__main__":
    main()
