#code
from Spider.DataCollector import DataCollector
from Spider.DataManager import DataManager
from Spider.downloader import Downloader
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from multiprocessing import Manager
import os
import time


# Get the content and save the data into the text file
def downloadAndSaveData(url,filename):

    # Download the page of this url
    print("Child process %s start to collecting comment" % os.getpid())
    downloader = Downloader()
    manager = DataManager()
    collector = DataCollector()
    urlContent = downloader.downloadHTML(url)
    comment = collector.getCotentOfComment(urlContent)

    # Save the contents into the file
    print("Save the data to the file...")
    manager.saveDataToFile(comment, filename)
    print("Child process %s finished the processing" % os.getpid())

    # Sleep for certain time to prevent from being banned
    time.sleep(3)




class SteamSpider(object):
    def __init__(self):
        self.downloader = Downloader()
        self.collector = DataCollector()
        self.manager = DataManager()
        self.commentSet = Manager().list()
        self.filename = "Comment.txt"
        self.crawlPage = 3


    def setCrawlPage(self, page):
        self.crawlPage = page


    def runSpider(self, gameCommentsUrl):
        # Get the comments set of a given game
        print("Collecting the link of pages")
        self.collector.crawlComments(self.crawlPage, gameCommentsUrl, self.commentSet)
        print("%d of link has been collected" %len(self.commentSet))

        # Get the actual contents the comments using
        # Multiprocessing
        print("Initializing the pool")
        pool = Pool(cpu_count())

        print("Collecting the comments...")
        for link in self.commentSet:
            pool.apply_async(downloadAndSaveData, args=(link, self.filename))

        print("Collection succeed !")
        pool.close()
        pool.join()
        print("Generating the wordcloud for the game")
        self.generateWordCloud()
        print("Generation succeed!")


    # Generate the word cloud image
    def generateWordCloud(self):
        # Get current dirname
        p = path.dirname("__dir__")

        # Open the text and image file for wordCloud generation
        f = open(path.join(p, self.filename), encoding="utf-8")

        try:
            print("Successfully open the file")
            text = f.read()

            # Initialize the wordcloud
            wordcloud = WordCloud().generate(text)

            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")

            wordcloud = WordCloud(max_font_size=40).generate(text)
            plt.figure()
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.show()

        finally:
            f.close()



