from bs4 import BeautifulSoup
import re
import requests
import os

"""
Small script to download all episodes of Learningmachines101 podcast.
"""


def grab_podcast_urls():
    pod_links = []

    for year in range(2014, 2020):
        url = f"https://www.learningmachines101.com/{year}"
        print(f"Page #{year}")
        page = requests.get(url)
        data = page.text
        soup = BeautifulSoup(data, "html.parser")
        laowaicast_links = soup.find_all("a", attrs={'href': re.compile("^(http|https)://traffic.libsyn.com/*"), "title": "Download"})
        for _ in laowaicast_links:
            link = _.get('href')
            print(link)
            pod_links.append(link)

    for url_pod in pod_links:
        download_episodes(url_pod)


def download_episodes(url_pod):
    r = requests.get(url_pod, allow_redirects=True)
    dirname = r".\learningmachines101_podcasts"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    else:
        pass
    filename, file_extension = os.path.splitext(os.path.basename(url_pod))
    print(f"File {filename}.mp3 is going to be downloaded.")
    open(f"{dirname}\\{filename}.mp3", 'wb').write(r.content)


if __name__ == "__main__":
    grab_podcast_urls()
    print("End of parsing!")
