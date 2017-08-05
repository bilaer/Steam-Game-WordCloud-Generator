from selenium import webdriver
from bs4 import BeautifulSoup
import time

class DataCollector(object):
    def __init__(self):
        pass

    def scrollDown(self, driver, pageNum):
        index = 0
        for i in range(pageNum):
            print("Scroll the %dth pages" %index)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            index = index + 1
            time.sleep(1)

    def selectEnglish(self, driver):
        ele = driver.find_element_by_id("filterlanguage")
        ele.click()
        eletwo = driver.find_element_by_id("filterlanguage_option_6")
        eletwo.click()

    def crawlComments(self, pageNum, url, commentSet):

        self.driver = webdriver.PhantomJS()
        self.driver.get(url)

        # Firstly select english
        self.selectEnglish(self.driver)

        # Then scroll down the web
        self.scrollDown(self.driver, pageNum)

        # Get the page source
        content = BeautifulSoup(self.driver.page_source, 'lxml')
        self.getComments(content, commentSet)


    def getComments(self, content, commentSet):
        soup = content.find("div", class_="apphub_Cards")
        for comment in soup.find_all("div", class_="apphub_Card modalContentLink interactable"):
            link = comment.get("data-modal-content-url")
            commentSet.append(link)
            print(link)
            print("current link: %d" %len(commentSet))

    # Get the contents ouf of comment page
    def getCotentOfComment(self, content):
        soup = BeautifulSoup(content.text, "lxml")
        text = soup.find("div", id="ReviewText")
        text = str(text.get_text())
        return text











