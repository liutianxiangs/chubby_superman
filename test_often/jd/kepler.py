#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*
import requests
class Http_request():
    def __init__(self,url,**kwargs):
        self.url = url
        self.kwargs=kwargs
    def update_port_datas(self):
        datas = {
        "method":"",
        "app_key":r'08e808ba00f34db5a1da36417400ab1b',
        'access_token':r'58e10eb1500c4726b59fcf6b7449d0c78',
        'timestamp':'2019-02-1416:13:10',
        'v':'1.0',
        'format':'json',
        'param_json':''
        }
        try:
            for k in self.kwargs:
                self.k=k
                datas[self.k]=self.kwargs[self.k]
        except Exception as e:
            print(e)
        return datas
    def post_request(self):
        datas =self.update_port_datas() #更新头部信息
        #print(datas)
        try:
            post_response =requests.post(url=self.url,data=datas)
            return post_response.text
        except Exception as e:
            print (e)
if __name__=="__main__":
    url = "https://router.jd.com/api"
    a = ["biz.product.sku.check","biz.product.state.query"]
    sku = 896023
    b = [r'{"skuIds":"%s"}'%sku,r'{ "sku": "%s"}'%sku]
    for i,j in zip(a,b):
        aa = Http_request(url,method=i,param_json=j).post_request()
        print(aa)


