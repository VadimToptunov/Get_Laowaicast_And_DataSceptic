from Downloader import PodcastDownloader as pdw
from os import path
import time
import shutil


class TestDummy:
    def test_grabbing_podcast_links(self, webpage, episode_link, attributes):
        pdw0 = pdw.PodcastDownloader()
        ex = pdw0.grabbing_links(webpage, attributes)
        assert episode_link in ex

    def test_create_directory_for_files(self, podlinks, podname):
        self.downloader(podlinks, podname)
        directory = f".\\{podname}_podcasts"
        assert path.isdir(directory)
        self.clean(directory)

    def test_downloading_files(self, podlinks, podname, filename):
        self.downloader(podlinks, podname)
        directory = f".\\{podname}_podcasts"
        assert path.isfile(f".\\{directory}\\{filename}")
        self.clean(directory)

    def downloader(self, pod_links, pod_name):
        pdw0 = pdw.PodcastDownloader()
        pdw0.downloader(pod_links, pod_name)
        time.sleep(10)

    def clean(self, directory):
        shutil.rmtree(directory)



