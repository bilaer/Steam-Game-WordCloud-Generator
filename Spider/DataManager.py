import os

class DataManager(object):
    def __init__(self):
        pass

    def saveDataToFile(self, string, filename):
        f = open(filename, "a+", encoding="utf-8")
        try:
            f.write(string)
        finally:
            f.close()
