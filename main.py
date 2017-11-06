# encoding=utf8
import requests
from bs4 import BeautifulSoup
import json
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):

        r = requests.get('https://bangumi.bilibili.com/web_api/timeline_global').json()
        for item in r['result']:
            if item['is_today'] == 1:
                today = item

        results = []

        for item in today['seasons']:
            res = {}
            pub_index = item['pub_index']
            url = 'https://bangumi.bilibili.com/anime/{}/play#{}'.format(item['season_id'], item['ep_id'])
            res["Title"] = item['title']
            res["SubTitle"] = "pub_index: " + str(pub_index)
            res["IcoPath"] = "Images\\bilibili.png"
            res["JsonRPCAction"] = {"method": "openUrl", "parameters": [url]}
            results.append(res)
        return results


    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
