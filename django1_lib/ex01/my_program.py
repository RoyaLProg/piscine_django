from local_lib import path

fileName = "readme"


def main():
    current = path.Path(fileName)
    current.touch()
    file = current.open(mode='w')
    file.write("something")
    file.close()
    file = current.open(mode='r')
    content = file.read()
    file.close()
    print(content)


if __name__ == "__main__":
    main()
