from Downloader import GetPods
from Downloader import PodcastDownloader


def run_downloader():
    get_pods = GetPods.GetPods()
    get_pods.choose_podcast(get_pods.choose_topic())


if __name__ == "__main__":
    run_downloader()
    print("End of parsing!")
    PodcastDownloader.PodcastDownloader.browser.quit()
