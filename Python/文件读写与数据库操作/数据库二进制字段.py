import sqlite3
import requests
# f = open('tmp.jpg','rb') 
# # 二进制打开图片
# img = f.read()
# f.close()
imgUrl = 'https://baike.baidu.com/pic/%E5%A1%94%E5%B8%8C%E5%AE%89%E5%A8%9C/18752054/0/c2fdfc039245d688d64e4689afc27d1ed21b244a?fr=lemma&ct=single#aid=0&pic=c2fdfc039245d688d64e4689afc27d1ed21b244a'
imgStream = requests.get(imgUrl, stream = True)
db = sqlite3.connect('sqltest.db')
cur = db.cursor()
sql = "update students set picture = ? where name = '李四' "
cur.execute(sql,(imgStream.content,))
# 多的逗号意味着元组