#!/usr/bin/python2
# -*- coding:UTF-8 -*-
 
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "students", charset='utf8' )
cursor = db.cursor()
id=275 
while id<306:
	sql="insert into students_info values("str(id)","Tom",'BJ',12);"
	print(sql)
	cursor.execute(sql)
	db.commit()
	id=id+1
db.close()
