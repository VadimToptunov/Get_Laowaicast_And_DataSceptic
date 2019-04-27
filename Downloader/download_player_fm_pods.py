"""
Topics:
	French:
		https://player.fm/series/learn-french-by-podcast
		https://player.fm/series/intermediate-french-podcast-2360552

	QA:
		https://player.fm/series/qa-guild-podcast
		https://player.fm/series/radio-qa
		https://player.fm/series/test-code-software-testing-development-python

	Python:
		https://player.fm/series/talk-python-to-me-python-conversations-for-passionate-developers-83399
		https://player.fm/series/the-python-podcast-init
		https://player.fm/series/python-bytes
		https://player.fm/series/import-this

	Data Science:
		https://player.fm/series/scalalaz-podcast-2149521

	Data Science & Machine Learning:
		http://dataskeptic.com/podcast?year={year}&limit=10&offset=30
		https://www.learningmachines101.com/{year}

	Laowaicast:
		https://laowaicast.ru/category/episode/page/{pagenum}

	Other:
		https://player.fm/series/superdatascience
		https://player.fm/series/series-2467644

"""

from bs4 import BeautifulSoup
import re
import requests
import os


class PodcastDownloader:
    def choose_topic(self):
        """
        Here a user chooses a topic of a podcast he/she wants to download.
        :return:
        """
        pass

    def choose_podcast(self):
        """
        Here a user chooses a specific podcast to download.
        :return:
        """
        podname = ""
        return podname

    def grab_podcast_urls(self, podname):
        """
        Parses podcast's download urls.
        :return:
        """
        dirname = f".\\{podname}_podcasts"
        self.download_podcast(dirname)

    def download_podcast(self, dirname):
        """
        Downloads podcast's episodes to a specific folder.
        :return:
        """
        pass