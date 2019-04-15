#__author__ = 'chubby_superman'  胖超人
#_*_coding=utf-8 _*
import pymysql

class db_ope():
    def __init__(self,host,user,password,port,lib):
        self.host=host
        self.user=user
        self.password=password
        self.lib=lib
        self.port=port
    # 连接数据库
    def get_db(self):
        db = pymysql.connect(self.host,self.user,self.password,self.lib,self.port,charset='utf8')
        return db
    #查询方法
    def select_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            data = cursor.fetchone()
        except Exception as e:
            print(e)
            database.rollback()
        print("查询结果\n",data)
        database.close()
        return data
    #插入方法
    def insertinto_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            #print("保存成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            raise e
            print("保存失败")
            database.rollback()
        database.close()
    def delete_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            print("删除成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            print(e)
            database.rollback()
        database.close()
    def updata_func(self,sql):
        database=self.get_db()
        cursor=database.cursor()
        try:
            cursor.execute(sql)
            database.commit()
            print("更新成功，影响%s行"%cursor.rowcount)
        except Exception as e:
            print(e)
            database.rollback()
        database.close()

if __name__ == "__main__":
    host = "rm-2ze6c2r3f406x926cxo.mysql.rds.aliyuncs.com"
    user = "pipitest"
    password = "abcd1234_"
    port = 3306
    lib = "pipitest"
    data_base=db_ope(host,user,password,port,lib)
    data_base.select_func("select * from shelf_goods WHERE id=11616")
    '''
    pymysql执行cursor.execute(sql)时可能会存在注入漏洞
    不推荐使用: sql='select * from userinfo where username="%s" and password="%s" ' %(user,pwd,)
    推荐使用  : sql = 'select * from userinfo where username=%s and password=%s',[user,pwd]
    本文可以改成这样：select_func('select * from userinfo where username=%s and password=%s',[user,pwd])
    '''
    data_base.insertinto_func("INSERT INTO shelf_activity_press(goods_id,goods_name,goods_image,period)"
                                                    " VALUES(11616,'test','a',10000)")
    '''
    1、需要注意，所执行的插入语句依然有可能出问题，例如报出：Warning: (1364, "Field 'period' doesn't have a default value")
    这是因为，数据表中，相对应的字段没有默认值，插入时需要设定，否则就会报错.另外，需要仔细对照字段的数据类型；
    2、有一个小坑，database=self.get_db()，因为连接数据库方法，每执行一次，就会建立并返回一个数据库连接，所以，在执行sql的时候
    应该是这样：连接数据库，获取游标，游标执行sql，提交。而不是这样：连接数据库，获取游标，游标执行sql，连接数据库，提交。
    '''

    data_base.updata_func("update shelf_activity_press set goods_name='tester' where period=10000")
    
    data_base.delete_func("DELETE FROM shelf_activity_press WHERE period=10000")
    '''
    1、sql中truncate，delete以及drop的区别，有兴趣的童鞋可以百度下，这里只用delete，从不建议数据库工程师以外的人
    使用drop和truncate。因为“从未拥有”远比“冗余”更可怕。
    2、sql中，使用删除时一定要加上where子句哦，否则很容易“被跑路”，也就是辞退，起码也要通报批评了。
    '''