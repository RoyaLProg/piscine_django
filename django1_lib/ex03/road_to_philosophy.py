from bs4 import BeautifulSoup
import requests
import sys

USAGE = f"USAGE: python3 {sys.argv[0]} WIKIPEDIA_URL"
START_PATTERN = "https://en.wikipedia.org/wiki/"


def test_link(link: str):
    if link.__contains__("Help:"):
        return False
    if link.__contains__("disambiguation"):
        return False
    if link.__contains__("Category"):
        return False
    if not link.startswith("/wiki/"):
        return False
    if link.__contains__("["):
        return False
    if link.__contains__("#"):
        return False
    return True


def get_next(url: str):
    # TODO: find next url in page
    # use beeautiful soup to extract all link
    # take first one that does not redirect to a dictionary page
    # (url !(containing current url
    #         || containing "Help"
    #         || or in italic
    #         || or not between in bracket
    # ))

    req = requests.get(url)
    if not req.ok:
        print("request returned a non ok response, terminating")
        exit(1)
    soup = BeautifulSoup(req.text, features='html.parser')
    soup = soup.find(id='mw-content-text')

    if len(soup.find_all('p')) < 2:
        return
    links_0 = soup.find_all('p')[0].find_all('a')
    links_1 = soup.find_all('p')[1].find_all('a')
    links = links_0 + links_1
    new_url = ""

    for link in links:
        if test_link(link['href']):
            new_url = 'https://en.wikipedia.org' + link['href']
            return new_url

    return new_url


def check_prevs(prevs: list, current: str):
    for p in prevs:
        if p == current:
            return False

    return True


def loop(url: str, prevs: list = []):
    if len(prevs) != 0:
        if not url.startswith(START_PATTERN):
            print(f"invalid url : {url}")
            return

    current = url.split('/')
    current = current[len(current) - 1]
    if url == START_PATTERN + "Philosophy":
        for road in prevs:
            print(road)
        print(f"{len(prevs)} roads from {prevs[0]} to philosophy !")
        exit(0)

    elif not check_prevs(prevs, current):
        print("It leads to an infinite loop !")
        exit(0)
    else:
        prevs.append(current)
        next = get_next(url)
        if type(next) is str:
            loop(next, prevs)
        print("It's a dead end !")
        exit(0)


def main():
    if len(sys.argv) != 2:
        print(USAGE)
        return

    search = sys.argv[1]
    url = START_PATTERN + search.lower().capitalize().replace(" ", "_")

    loop(url)


if __name__ == "__main__":
    main()
