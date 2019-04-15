#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*
from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl
import time
from compiler.ast import flatten
def h5_se(page):
    driver = webdriver.Firefox()
    try :
        driver.get("https://list.jd.com/list.html?cat=12218,13553,13576&page=%d&delivery=1"%page)
        driver.refresh()
        time.sleep(2)
    except Exception as e:
        pass
    time.sleep(2)
    a = driver.page_source
    driver.close()
    return a
def sku(soup):
    #获取sku
    sku1 = soup.select('li.gl-item div.gl-i-wrap.j-sku-item')
    sku = []
    for i in sku1:
        i=i["data-sku"]
        sku.append(i)
    #获取商品名称
    name1 = soup.select("li.gl-item div.gl-i-wrap.j-sku-item div.p-name a em")
    name = []
    for i in name1:
        i=i.getText()
        name.append(i)
    #获取价格
    price1 = soup.select("li.gl-item div.gl-i-wrap.j-sku-item div.p-price strong.J_price.js_ys i")
    price = []
    for i in price1:
        i = i.get_text()
        price.append(i)
    #获取商品标签。例：京东自营，满减，满赠，放心购，险等等
    goods_label= soup.select("li.gl-item div.gl-i-wrap.j-sku-item div.p-icons.J-pro-icons")

    goods_labels=[]
    for i in goods_label:
        i = i.getText()
        goods_labels.append(i)
    return sku,name,price,goods_labels
a = []
for i in range(1):
    soup = BeautifulSoup(h5_se(i+1),"lxml")
    a.append(sku(soup))
c = []
for i in range(len(a)):
    for j in range(len(a[i])):
       c.append(a[i][j])
sku=[]
name = []
pr = []
biao =[]
for i in range(len(c)+1):
    if i%4==1:
        sku.append(c[i-1])
    elif i%4==2:
        name.append(c[i-1])
    elif i%4==3:
        pr.append(c[i-1])
    else:
        if i ==0:
            pass
        else:
            biao.append(c[i-1])
sku = [g for i in sku for g in i]
name = [g for i in name for g in i]
pr = [g for i in pr for g in i]
biao = [g for i in biao for g in i]
data = [sku,name,pr,biao]
workbook=openpyxl.load_workbook(r"E:\test\jaasdf.xlsx")
sheet = workbook.get_active_sheet()
for i in range(len(data)):
    for j in range(len(data[i])):
        sheet.cell(row =j+1,column =i+1,value =data[i][j])
workbook.save("jaasdf.xlsx")
