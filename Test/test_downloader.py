from Test import Testdummy
from Downloader import PodcastDownloader as pdw
import re

laowaicast_attributes = {'href': re.compile("^(http|https)://media.*"), "title": "Скачать"}
laowaicast_webpage = "https://laowaicast.ru/category/episode/page/2/"
laowaicast = "laowaicast"


def test_grabbing_laowaicast_links():
    dum = Testdummy.TestDummy()
    laowaicast_link = "https://media.blubrry.com/laowaicast__/s/audio.simplecast.com/afdcd351.mp3"
    dum.test_grabbing_podcast_links(laowaicast_webpage, laowaicast_link, laowaicast_attributes)


def test_download_laowaicast_file():
    dum = Testdummy.TestDummy()
    pdw0 = pdw.PodcastDownloader()
    ex = pdw0.grabbing_links(laowaicast_webpage, laowaicast_attributes)
    dum.test_downloading_files(ex, laowaicast, "028f9f95.mp3")


def test_create_laowaicast_directory_download():
    dum = Testdummy.TestDummy()
    pdw0 = pdw.PodcastDownloader()
    ex = pdw0.grabbing_links(laowaicast_webpage, laowaicast_attributes)
    dum.test_create_directory_for_files(ex, laowaicast)

