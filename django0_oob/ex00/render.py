import sys
from settings import *


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def verifyName(fileName):
    if not fileName.endswith('.template'):
        print("not a .template file")
        return False
    return True


def openOutput(fileName):
    file = open(rreplace(fileName, ".template", ".html", 1), 'w')
    return file


def render(file, output):
    lines = file.readlines()

    for line in lines:
        try:
            line = line.format(**globals())
        except:
            line = line
        finally:
            output.write(line)
    return


def main():
    argv = sys.argv[1::]
    if len(argv) != 1:
        print("Wrong number of argument")
        return
    filename = argv[0]
    if not verifyName(filename):
        return
    try:
        file = open(filename)
    except:
        print(f"{filename} does not exist")
        return
    try:
        output = openOutput(filename)
    except:
        outputFileName = rreplace(filename, '.template', '.html', 1)
        print(f"{outputFileName} could not be opened/created")
        return
    render(file, output)
    file.close()


if __name__ == '__main__':
    main()
