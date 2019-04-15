#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*


import schedule
import pymysql

def sql_test_database(count):
    host = "rm-2ze6c2r3f406x926cxo.mysql.rds.aliyuncs.com"
    user = "pipitest"
    password = "abcd1234_"
    lib = "pipitest"
    db = pymysql.connect(host,user,password,lib)
    cursor = db.cursor()
    try:
        cursor.execute("delete  from shelf_activity_press_record")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    count=count+1


schedule.every(5).seconds.do(sql_test_database,0)#每隔5秒执行sql_test_database方法
#schedule.every(5).minutes.do(sql_test_database)#每隔五分钟执行sql_test_database方法
#schedule.every(5).hours.do(sql_test_database)#每隔5小时执行sql_test_database方法

if __name__ == '__main__':
    while 1:
        schedule.run_pending()

