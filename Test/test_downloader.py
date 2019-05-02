from Downloader import GetPods
from Downloader import PodcastDownloader as pdw
import re


def test_grab_podcast_urls():
    attributes = GetPods.GetPods.laowaicast_attributes
    ex = pdw.PodcastDownloader.grab_podcast_urls("laowaicast", "https://laowaicast.ru/category/episode/page/",
                                                 2, 1, -1, attributes)
    assert ex != []
