from Spider.SteamSpider import SteamSpider


if __name__ == "__main__":
    test = SteamSpider()
    test.setCrawlPage(500)
    test.runSpider("http://steamcommunity.com/app/620/reviews/?browsefilter=toprated&snr=1_5_reviews_ ")



