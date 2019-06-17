#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Backup Database from Mysql or Mariadb
"""

import os
import time
import pymysql


class BackupDB:
	"""Backup user`s Databases"""
	def __init__(self, servername, value):
		"""初始化属性"""
		self.servername = servername
		self.host = value[0]
		self.username = value[1]
		self.password = value[2]
		try:
			self.port = value[3]
		except:
			self.port = 3306


		# 连接成功与否
		self.connected = False

		# 备份命令路径
		self.mysqldump = '/usr/local/mysql/bin/mysqldump'
		# 备份目录
		self.backup_dir = '/Volumes/WorkData/数据库备份/'
		# 当前时间
		self.time_now = time.strftime("%Y%m%d%H%M", time.localtime())
		# mysql默认数据库
		self.sys_dbs = ("mysql", "information_schema", "test", "performance_schema", "sys")

		# 连接数据库
		self.connect_db()
		# 备份数据库
		#self.dump_db()

	def connect_db(self):
		"""连接到数据库，获取所有数据库名"""
		# 打开数据库连接
		try:
			print("正在连接 %s ……" % self.servername)
			self.db = pymysql.connect(
				host=self.host,
				port=self.port,
				user=self.username,
				passwd=self.password
				)

			self.connected = True
		except:
			print("[ %s ] 连接失败，未备份！" % self.servername)
			#exit()  # 连接失败退出任务
			return False

	def get_db_names(self):
		"""获取数据库列表"""
		# 创建游标
		cur = self.db.cursor()
		cur.execute("show databases")

		# 格式为每个库名一个tuple组成的一个tuple：
		#(('information_schema',), ('apkcenter',), ('blockchain',), ……)
		return cur.fetchall()

	def dump_cmd(self, db_name, badkup_filename):
		"""备份的命令"""
		print("正在备份 %s.%s ……" % (self.servername, db_name))
		os.system(
			"""
			{mysqldump} -u{username} -p{password} -h {host} -P {port} ‘{db_name}’ | gzip > {badkup_filename}.gz
			""".format(
					mysqldump=self.mysqldump,
					username=self.username,
					password=self.password,
					host=self.host,
					port=self.port,
					db_name=db_name,
					badkup_filename=badkup_filename,
					)
		)


	def dump_db(self):
		"""备份所有数据库"""
		db_names = self.get_db_names()  # 数据库列表

		# 为服务器创建一个单独的文件夹存放备份
		backup_dir0 = self.backup_dir + self.servername + '/'
		if not os.path.exists(backup_dir0):
			os.makedirs(backup_dir0)
		# 备份所有用户数据库
		for row in db_names:
			if not row[0] in self.sys_dbs:  # 排除系统默认数据库
				# 创建一个数据名字的文件夹存放备份
				backup_dir1 = backup_dir0 + row[0] + '/'
				if not os.path.exists(backup_dir1):
					os.makedirs(backup_dir1)
				#print(row[0])
				badkup_filename = backup_dir1 + self.time_now + '.sql'
				#print(badkup_filename)
				# 当前时间
				self.time_now = time.strftime("%Y%m%d%H%M", time.localtime())
				# 执行备份
				self.dump_cmd(row[0], badkup_filename)

				print("%s.%s 备份完成！" % (self.servername, row[0]))


	def __del__(self):
		"""退出时关闭数据库连接"""
		if self.connected:
			self.db.close()

if __name__ == '__main__':
	hosts = {

		"db_摩氪头条": ("47.75.128.266", "root", r"HwFJUjgtB6q5Z^o8"),
		"db_摩头条": ("47.75.128.256", "root", r"HwFJUjgtB6q5Z^o8")
	}



	for key,value in hosts.items():
		dm = BackupDB(key, value)
		if dm.connected:
			dm.dump_db()

