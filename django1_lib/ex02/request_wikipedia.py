import requests
import dewiki
import sys

API_URL = "https://en.wikipedia.org/w/api.php"
USAGE = f"Usage : {sys.argv[0]} \"query\""
HEADERS = {'User-Agent': 'Mozila/5.0 (Linux; Android 14; SM-S928W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36'}


def write_to_file(pageTitle: str, content: str):
    filename = sys.argv[1].lower().replace(" ", "_") + ".wiki"
    unwikied_content = dewiki.from_string(content)
    file = open(filename, "w")

    file.write(unwikied_content)
    file.close()


def get_page(pageTitle: str):
    res = requests.api.get("https://en.wikipedia.org/w/index.php",
                           [("title", pageTitle), ("action", "raw")], headers=HEADERS)

    if not res.ok:
        print("page does not exist")
        return

    content = res.text
    write_to_file(pageTitle, content)


def search(string: str):
    res = requests.api.post(API_URL, [("action", "query"), ("list", "search"),
                                      ("srsearch", string), ("format", "json")], headers=HEADERS)
    if not res.ok:
        print(res.request.body)
        print(res)
        print("request failed")
        return

    try:
        res_json = res.json()
        pageTitle = res_json["query"]["search"][0]["title"]
        get_page(pageTitle)
    except ValueError:
        print("response did not contain valid json")
        return
    except IndexError:
        print("no result found")
        return


def main():
    if len(sys.argv) != 2:
        print(USAGE)
        return
    query = sys.argv[1]
    search(query)


if __name__ == "__main__":
    main()
