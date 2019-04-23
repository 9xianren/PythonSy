import requests
import lxml
from lxml import etree
import csv
import pymysql

class Spider:
    def __init__(self,version):
        self.version = version
        self.result = []
        
    def get_page(self,start_num):
        url='https://movie.douban.com/top250?start=%s&filter=' % start_num
        res=requests.get(url)

        tree=etree.HTML(res.text)
        top205=tree.xpath('//span[@class="title"][1]/text()')
        print(top205)
        return top205
    def go(self):
        print("Start..")
        for i in range(0,2):
            top250=self.get_page(i*25)
            self.result +=top250
            
        return self.result

if __name__=="__main__":
    my_spider=Spider('1.0')
    res=my_spider.go()
    db=pymysql.connect("localhost","root","123456","test")
    cursor=db.cursor()
    sql="INSERT INTO testmodel_test(name) VALUES (%s)"
    for a in res:
        cursor.execute(sql,(a))
        db.commit()
    db.close()

def getImage():
    my_spider=Spider('1.0')
    res=my_spider.go()
    db=pymysql.connect("localhost","root","123456","test")
    cursor=db.cursor()
    sql1="truncate table testmodel_test"
    cursor.execute(sql1)
    sql="INSERT INTO testmodel_test(name) VALUES (%s)"
    for a in res:
        cursor.execute(sql,(a))
        db.commit()
    db.close()
