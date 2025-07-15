import sys

USAGE = f"""
Usage : {sys.argv[0]} longitude latitude md5(YYYY-DD-MM-opening_dow)

    get opening dow: http://geo.crox.net/djia/%Y/%m/%d
    replace %Y %m %d with appropriate values
"""


def main():
    args = sys.argv[1::]

    if len(args) < 3:
        print(USAGE)
        return

    long = args[0]
    lat = args[1]
    hash = args[2]

    if len(hash) != 32:
        print("ERROR: hash should be 128 bytes (32 chars) long")
        return
    try:
        float(long)
    except ValueError:
        print("ERROR: longitude is not decimal")
        return
    try:
        float(lat)
    except ValueError:
        print("ERROR: latitude is not decimal")
        return
    try:
        int(hash, 16)
    except ValueError:
        print("ERROR: hash is not hexadecimal")
        return

    parts = [int(hash[0:16:], 16), int(hash[16::], 16)]
    left = str(long.split('.')[0]) + '.' + str(parts[0])[0:6]
    right = str(long.split('.')[0]) + '.' + str(parts[1])[0:6]

    print(left, right)


if __name__ == "__main__":
    main()
