from bs4 import BeautifulSoup
import lxml
import requests
import spotipy_OAuth

BASE_URL = "https://www.billboard.com/charts/hot-100/"
DATA_FILE = "./data/hot_100.html"


def get_web_page(url):
    # Get web page
    response = requests.get(url)

    # Save web page to file
    with open(DATA_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.text)


def read_web_file(url):
    try:
        open(DATA_FILE)
    except FileNotFoundError:
        get_web_page(url)
    else:
        pass
    finally:
        # Read the web page from file
        with open(DATA_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


def get_all_titles(soup):
    # Get all article HTML elements
    all_titles = soup.findAll(class_="chart-element__information__song text--truncate color--primary")
    title_texts = []
    for title in all_titles:
        text = title.getText()
        title_texts.append(text)
    return title_texts


if __name__ == "__main__":
    # date_reqd = input("What date do you want to go to? (YYYY-MM-DD)\n")
    # # Get a snapshot of the web page
    # web_page = BASE_URL + date_reqd
    # result = read_web_file(web_page)
    # titles = get_all_titles(result)
    # print(titles)

    spotipy_OAuth.authorization_flow()
