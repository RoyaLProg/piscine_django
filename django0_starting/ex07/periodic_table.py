def displayCell(name, line):
    # line content :
    #   position ([0 - 18[)
    #   atomic number
    #   letter(s)
    #   molar mass
    #   electrons (not sure what it represent)

    rv = f"""
                <div style="height: 100px; width: 100px; border: black 1px solid;">
                   <h4 style="font-size: 10px">{name}</h4><br>
                   <p style="font-size: 9px;"><span style="font-weight: bold;">{line["small"]}</span>, {line["number"]}, {line["molar"]}</p>
                </div>
        """
    return rv


def displayContent(content):
    rv = ""
    last = 0
    for key in content:
        line = content.get(key)
        current = int(line["position"])
        if current > last:
            for i in range(last, current - 1):
                rv += "<div></div>"
        last = current
        rv += displayCell(key, line)
    return rv


def format(content):
    rv = {}
    for row in content:
        if not len(row):
            continue
        x = row.split(" = ")
        y = x[1].split(',')
        dict2 = {}
        for info in y:
            info = info.split(':')
            dict2.update({info[0].strip(): info[1]})
        rv.update({x[0]: dict2})
    return rv


def main():
    file = open("periodic_table.txt")
    content = file.read().split('\n')
    file.close()

    content = format(content)

    out = """
            <!DOCTYPE html>
            <html lang='en' style="margin: 0">
                <head>
                    <title>Periodic table</title>
                    <meta charset="utf-8">
                </head>
                <body style="margin: 0; display: flex; width: 100dvw; height: 100dvh;">
                    <main style="display: grid; grid-template-columns: repeat(18, 1fr); margin: auto;text-align: center">
        """

    out += displayContent(content)

    out += """
                    </main>
                </body>
            </html>
        """
    print(out)


if __name__ == "__main__":
    main()
