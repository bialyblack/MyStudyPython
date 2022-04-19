"""from bmi import *

fun_bmi("依依",1.75,120)
def fun_bmi(person,height,weight):
    person="22"
    height=33
    weight=12
    print("哈哈",person,height,weight)
fun_bmi("ok",22,33)
import sys
print(sys.path)
import christmastree as m
print(m.pinetree)"""


from dataclasses import dataclass
from unittest import result
import setting.size
if __name__=='__main__':
    print(setting.size.width)
    print(setting.size.height)
'''
file=open('picture.png','rb')
print(file)'''
"""print('\n','='*10,"蚂蚁庄园动态",'='*10)
with open('message.txt','w') as fifle:
    pass
print('\n即将显示...\n')"""
'''
#与文件编码有影响
with open('b.txt','r') as file:
   
    file.seek(2)
    string=file.read(9)
    print(string)

'''
"""print('\n','='*35,"蚂蚁庄园动态",'='*35)
with open('message.txt','r') as file:
        print(file.readlines())"""
        



"""   number=0
    while True:
        number=1
        line=file.readline()
        if line == '':
            break
        """

'''print('\n','='*35,"蚂蚁庄园动态",'='*35)
with open('message.txt','r') as file:
        messageall=file.readlines()
        for message in messageall:
            print(message)'''
'''import os
print(os.name)
print(os.sep)'''
'''print(os.linesep)
print(os.getcwd())
with open('源码/上册138个/11/message.txt') as file:
    pass
print(os.path.abspath(r"源码\上册138个\11\message.txt'"))
if not os.path.exists('C:\\demo'):
    os.mkdir("C:\\demo")
else:
    print(os.path.exists('C:\\demo'),"目录已经存在")'''

'''if not os.path.exists('C:\\demo\\test\\dir\\mr'):
    os.makedirs("C:\\demo\\test\\dir\\mr")

else:
    print(os.path.exists('C:\\demo\\test\\dir\\mr'),"目录已经存在")'''

'''if os.path.exists('C:\\demo\\test\\dir\\mr'):
   print(os.path.exists('C:\\demo\\test\\dir\\mr'))
   os.rmdir('C:\\demo\\test\\dir\\mr')
else:
     print("删除成功")'''
"""import shutil
shutil.rmtree('C:\\demo\\test')"""
'''tuples=os.walk("E:\\python_code\\源码\\上册138个\\01")
for tuple in tuples:
    print(tuple,"\n")'''
"""if os.path.exists('b.txt'):
    os.remove("b.txt")
    print("文件删除完毕")"""
'''src="C:\\demo\\test\\dir\\mr\\b.txt"
#os.rename(src,"C:\\demo\\test\\dir\\mr\\a.txt")
if os.path.exists(src):
    os.rename(src,"C:\\demo\\test\\dir\\mr\\a.txt")
    print("文件重命名完毕")
else:
    print("文件不存在")'''
'''src="demo"
if os.path.exists(src):
    os.rename(src,"text")
    print("目录重命名完毕")
else:
    print("目录不存在")
print(os.stat("C:\\demo\\test\\dir\\mr\\a.txt"))'''

'''import sqlite3
conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
#cursor.execute('create table user (id int(10) primary key,name varchar(20))')
#cursor.execute('update user set name=? where id= ?',('MR','1'))
cursor.execute('delete from  user where id=?',(1,))
cursor.execute('select * from user')
#cursor.execute('select * from user where id >1 ')
result1=cursor.fetchall()
print(result1)
cursor.close()
conn.commit()
conn.close()'''

'''import pymysql
db=pymysql.connect(host='localhost',user='root',password='asdfghjkl',db='mrsoft')
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
cursor.execute('DROP TABLE IF EXISTS books')
sql="""CREATE TABLE books 
(id int(8) NOT NULL AUTO_INCREMENT,
name varchar(50) NOT NULL,
category varchar(50) NOT NULL,
price decimal(10,2) DEFAULT NULL,
publish_time date DEFAULT NULL,
PRIMARY KEY(id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;        """
cursor.execute(sql)

#data=cursor.fetchone()
#print(data)
db.close()'''

import pymysql
db=pymysql.connect(host='localhost',user='root',password='asdfghjkl',db='mrsoft',charset="utf8")
cursor=db.cursor()
data=[("零基础学Python",'Python','79.80','2018-5-20'),
        ("Python从入门到精通",'Python','69.80','2018-6-18'),
        ("零基础学PHP",'PHP','69.80','2017-5-21'),
        ("PHP项目开发实战入门",'PHP','79.80','2016-5-21'),
        ("零基础学Java",'java2','69.80','2017-5-21'),
        ]
try:
    cursor.executemany("insert into books(name,category,price,publish_time)values (%s,%s,%s,%s)",data)
    #cursor.executemany("insert into books(name, category, price, publish_time)values  (%s,%s,%s,%s)", data)
    db.commit()
except:
    db.rollback()
db.close()