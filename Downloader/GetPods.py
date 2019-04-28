import Downloader.PodcastDownloader as pdw
import re


class GetPods:
    media = re.compile("^(http|https)://media.*")
    libsyn = re.compile("^(http|https)://traffic.libsyn.com/*")

    datasceptic_attributes = {'href': libsyn}
    laowaicast_attributes = {'href': media, "title": "Скачать"}
    learningmachines_attributes = {'href': libsyn, "title": "Download"}

    def choose_topic(self):
        """
        Here a user chooses a topic of a podcast he/she wants to download.
        :return: user_answer
        """

        text = """
        Hello, user! You are going to download a podcast. \n
        Which topic would you like to choose? \n\n
        [0] Data Science \n
        [1] Data Science & Machine Learning \n
        [2] French \n
        [3] Laowaicast \n
        [4] Python \n
        [5] QA \n
        [6] Java & Scala \n
        """
        return input(text)

    def choose_podcast(self, user_answer):
        """
        Here a user chooses a specific podcast to download.
        :return:
        """
        text0 = "Please, choose a podcast: \n"
        data_science = "[0] Super Data Science \n"
        data_science_machine_learning = """
        [0] DataSckeptic \n
        [1] Learningmachines101 \n
        """
        laowaicast = "[0] Laowaicast \n"
        python = """
        [0] Talk Python To Me \n
        [1] The Python podcast.__init__ \n
        [2] Python Bytes \n
        [3] Import This \n
        """
        qa = """
        [0] QA Guild \n
        [1] Radio QA \n
        [2] Test and Code \n
        """

        java_scala = """
        [0] Scalalaz \n
        [1] Razbor Poletov \n
        """
        french = """
        [0] Learn French By Podcast \n
        [1] Intermediate French \n
        """
        downloader = pdw.PodcastDownloader()

        if user_answer == "0":
            answer = input(f"{text0}{data_science}")
            if answer == "0":
                self.get_pfm(downloader, "superdatascience")
            else:
                print("Sorry, wrong number!")
        elif user_answer == "1":
            answer = input(f"{text0}{data_science_machine_learning}")
            if answer == "0":
                downloader.grab_dataskeptic_urls(2014, 2020, 1, self.datasceptic_attributes)
            elif answer == "1":
                downloader.grab_podcast_urls("learningmachines101", "https://www.learningmachines101.com/",
                                                        2014, 2020, 1, self.learningmachines_attributes)
            else:
                print("Sorry, wrong number!")
        elif user_answer == "2":
            answer = input(f"{text0}{french}")
            if answer == "0":
                self.get_pfm(downloader, "learn-french-by-podcast")
            elif answer == "1":
                self.get_pfm(downloader, "intermediate-french-podcast-2360552")
            else:
                print("Sorry, wrong number!")
        elif user_answer == "3":
            answer = input(f"{text0}{laowaicast}")
            if answer == "0":
                downloader.grab_podcast_urls("laowaicast", "https://laowaicast.ru/category/episode/page/",
                                                        25, 1, -1, self.laowaicast_attributes)
            else:
                print("Sorry, wrong number!")
        elif user_answer == "4":
            answer = input(f"{text0}{python}")
            if answer == "0":
                self.get_pfm(downloader, "talk-python-to-me-python-conversations-for-passionate-developers-83399")
            elif answer == "1":
                self.get_pfm(downloader, "the-python-podcast-init")
            elif answer == "2":
                self.get_pfm(downloader, "python-bytes")
            elif answer == "3":
                self.get_pfm(downloader, "import-this")
            else:
                print("Sorry, wrong number!")
        elif user_answer == "5":
            answer = input(f"{text0}{qa}")
            if answer == "0":
                self.get_pfm(downloader, "qa-guild-podcast")
            elif answer == "1":
                self.get_pfm(downloader, "radio-qa")
            elif answer == "2":
                self.get_pfm(downloader, "test-code-software-testing-development-python")
            else:
                print("Sorry, wrong number!")
        elif user_answer == "6":
            answer = input(f"{text0}{java_scala}")
            if answer == "0":
                self.get_pfm(downloader, "scalalaz-podcast-2149521")
            elif answer == "1":
                self.get_pfm(downloader, "series-2467644")
            else:
                print("Sorry, wrong number!")
        else:
            print("Sorry, wrong number!")

    def get_pfm(self, downloader, podname):
        downloader.grab_podcast_urls_pfm(podname)


if __name__ == "__main__":
    answer = GetPods.choose_topic()
    GetPods.choose_podcast(answer)
    print("End of parsing!")
