#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*


from locust import HttpLocust,TaskSet,task
import gevent
gevent.sleep(1)

class Baidu(TaskSet):

    @task(1)
    def test1(self):
        url="/"
        header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
        req1 = self.client.get(url,header)
        if req1==200:
            print("1,success")
        else:
            print("1,fails")
    @task(2)
    def test2(self):
        url="/"
        header ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
        req2 = self.client.post(url,header)
        if req2 ==200:
            print("2,success")
        else:
            print("2,fails")

class web_user(HttpLocust):
    task_set=Baidu
    min_wait=3000
    max_wait=6000
if __name__=="__main__":
    import os
    os.system("locust -f C:/Users\Administrator\Desktop\lalala\chubby_superman\locust\locust_start\demo_locust.py --host=http://www.baidu.com")