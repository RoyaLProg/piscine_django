import sys
import antigravity

USAGE = f"""
Usage : {sys.argv[0]} longitude latitude md5(YYYY-DD-MM-opening_dow)

    get opening dow: http://geo.crox.net/djia/%Y/%m/%d
    replace %Y %m %d with appropriate values
"""


def checkDate(date: str):
    parts = date.split('-')

    if len(parts) != 4:
        raise ValueError()
    if len(parts[3]) != 8:
        raise ValueError()

    testDow = parts[3].split('.')

    if len(testDow) != 2:
        raise ValueError()
    if len(testDow[1]) != 2:
        raise ValueError()

    int(parts[0])
    int(parts[1])
    int(parts[2])
    float(parts[3])


def main():
    args = sys.argv[1::]

    if len(args) < 3:
        print(USAGE)
        return

    long = args[0]
    lat = args[1]
    date = args[2].encode('utf-8')

    if len(date) != 19:
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
    # try:
    #     checkDate(date)
    # except ValueError:
    #     print("ERROR: hash is not hexadecimal")
    #     return

    antigravity.geohash(float(lat), float(long), date)
    # myHash = f"{hash(date)}"
    # print(myHash)
    # parts = [float.fromhex("0." + myHash[0:16:]), float.fromhex("0." + myHash[16::])]
    # left = str(long.split('.')[0]) + '.' + str(parts[0])[0:6]
    # right = str(long.split('.')[0]) + '.' + str(parts[1])[0:6]
    #
    # print(left, right)


if __name__ == "__main__":
    main()
