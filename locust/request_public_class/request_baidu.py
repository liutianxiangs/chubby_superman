#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*

import requests

url="http://www.baidu.com/"
heard ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
class request_mthod():
    def __init__(self,url,heard):
        self.url=url
        self.heard=heard
    def get_request(self):
        req = requests.get(self.url,heards=self.heard)
        print(req)
        print(req.text.encode("utf-8"))
    def post_request(self):
        req = requests.post(self.url,data='',headers=self.heard)
        print(req)
        print(req.text.encode("utf-8"))
if __name__=="__main__":
    request_mthod(url,heard).post_request()
    request_mthod(url,heard).post_request()

