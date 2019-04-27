from bs4 import BeautifulSoup
import os
import re
import requests
from selenium import webdriver
import time

"""
Small script to download all episodes of DataSceptic podcast.
"""


browser = webdriver.Chrome(r".\chromedriver.exe")


def grab_podcast_urls():
    pod_links = []
    for year in range(2014, 2020):
        url = f"http://dataskeptic.com/podcast?year={year}&limit=10&offset=30"
        browser.get(url)
        browser.set_window_position(-2000, 0)
        time.sleep(30)
        print(f"Page #{year}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        links = soup.find_all("a", attrs={'href': re.compile("^(http|https)://traffic.libsyn.com/*")})
        for _ in links:
            link = _.get('href')
            pod_links.append(link)
            print(link)

    for url_pod in pod_links:
        download_dataskeptic(url_pod)


def download_dataskeptic(url_pod):
    r = requests.get(url_pod, allow_redirects=True)
    dirname = r".\dataskeptic_podcasts"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else: pass
    filename, file_extension = os.path.splitext(os.path.basename(url_pod))
    print(f"File {filename}.mp3 is going to be downloaded.")
    open(f"{dirname}\\{filename}.mp3", 'wb').write(r.content)


if __name__ == "__main__":
    grab_podcast_urls()
    print("End of parsing!")
    browser.quit()

