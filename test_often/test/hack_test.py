#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*

import time
import random,string
from database import pymysql_test

host = "rm-2ze6c2r3f406x926cxo.mysql.rds.aliyuncs.com"
user = "pipitest"
password = "abcd1234_"
port = 3306
lib = "pipitest"
db = pymysql_test.db_ope(host,user,password,port,lib)


#向数据库插入数据方法
def t_thread(id):
    print(time.strftime('%Y.%m.%d ,%H,%M,%S',time.localtime(time.time())))
    x = (x for x in range(1,id+1))
    k = int(id/10)
    for i in range(k):
        sql ="INSERT INTO chubby_superman_test (j_id,test_name,image,phone) VALUES(%d,'test','aasdfsf'," \
             "10000)"%((next(x),next(test_name_auto()),))
        for j in range(10-1):
            sql = sql+","+"(%d,'test','asf',10000)"%(next(x))
        try:
            db.insertinto_func(sql)
        except Exception as e:
            print(e)
            time.sleep(1)
    print(time.strftime('%Y.%m.%d ,%H,%M,%S',time.localtime(time.time())))
#t_thread(100)

#test_name生成函数，生成器,返回类型为字符串
def test_name_auto():
    x =[x for x in range(100,201,10)]
    y =[y for y in range(200,301,10)]
    while 1:
        z = random.choice(x+y)
        z = str(z)
        yield z
#image生成函数，返回类型为字符串

def image_auto():
    #s = string.ascii_lowercase #所有小写字母(a-z)
    #s=string.ascii_letters #所有大小写字母(a-z,A-Z)
    #s=string.ascii_uppercase #所有大写字母(A-Z)
    s = string.ascii_letters
    r = random.choice(s)
    http = "http://qiniuyun.com/"
    for i in range(5):
        r = r+str(random.randint(0,9))+random.choice(s)
    print(http+r+str(time.time()).replace(".","")[3:])
    print(r)

image_auto()