"""
Gets a list of songs for a given year from billboard.com
"""

DATA_FILE = ""


def get_web_page(date_reqd):
    """
    Read web page for a given year and save to file.

    :param date_reqd: string YYYY-MM-DD
    :return: nothing
    """

    import requests

    # Get a snapshot of the web page
    url = "https://www.billboard.com/charts/hot-100/" + date_reqd

    # Get web page
    response = requests.get(url)

    # Save web page to file
    with open(DATA_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.text)


def read_web_file(date_reqd):
    """
    Read web page from file. If no file, then get new snapshot.

    :param date_reqd: string YYYY-MM-DD
    :return: BeautifulSoup object
    """

    from bs4 import BeautifulSoup
    # import lxml

    global DATA_FILE
    DATA_FILE = f"./data/{date_reqd}.html"

    try:
        open(DATA_FILE)
    except FileNotFoundError:
        get_web_page(date_reqd)
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

    # Get all song title HTML elements
    # ############# Billboard has changed! #############
    # all_titles = soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")
    all_titles = soup.find_all("h3", id="title-of-a-story", class_="a-font-primary-bold-s")
    # title_texts = []
    # for title in all_titles:
    #     text = title.getText().strip()
    #     title_texts.append(text)
    title_texts = [title.getText().strip() for title in all_titles]

    return title_texts


def get_song_titles(date_reqd):
    """
    Read web page from file if it already exists, else get new snapshot of the web page.

    :param date_reqd: string YYYY-MM-DD
    :return: list of song titles
    """

    result = read_web_file(date_reqd)
    titles = get_all_titles(result)
    # print(titles)
    return titles


if __name__ == "__main__":
    songs = get_song_titles("2008-08-08")
    print(songs)
