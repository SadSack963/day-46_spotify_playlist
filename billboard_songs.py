"""
Gets a list of songs for a given year from billboard.com
"""

DATA_FILE = "./data/hot_100.html"


def get_web_page():
    """
    Read web page for a given year and save to file.

    :return: nothing
    """

    import requests

    date_reqd = input("What date do you want to go to? (YYYY-MM-DD): ")
    # Get a snapshot of the web page
    url = "https://www.billboard.com/charts/hot-100/" + date_reqd

    # Get web page
    response = requests.get(url)

    # Save web page to file
    with open(DATA_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.text)


def read_web_file():
    """
    Read web page from file. If no file, then get new snapshot.

    :return: BeautifulSoup object
    """

    from bs4 import BeautifulSoup
    # import lxml

    try:
        open(DATA_FILE)
    except FileNotFoundError:
        get_web_page()
    else:
        pass
    finally:
        # Read the web page from file
        with open(DATA_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


def get_all_titles(soup):
    """
    Find all song titles on the given web page.

    :param soup: BeautifulSoup object
    :return: list of song titles
    """

    # Get all article HTML elements
    all_titles = soup.findAll(class_="chart-element__information__song text--truncate color--primary")
    title_texts = []
    for title in all_titles:
        text = title.getText()
        title_texts.append(text)
    return title_texts


def get_song_titles():
    """
    Read web page from file if it already exists, else get new snapshot of the web page.

    :return: list of song titles
    """

    result = read_web_file()
    titles = get_all_titles(result)
    # print(titles)
    return titles
