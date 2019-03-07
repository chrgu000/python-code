#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Backup Database from Mysql or Mariadb
"""

import os
import time
import pymysql
import threading


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
		self.connected = True


		# 备份命令路径
		self.mysqldump = '/usr/local/mysql/bin/mysqldump'
		# 备份目录
		self.backup_dir = '/Volumes/WorkData/数据库备份/'
		# 当前时间
		self.time_now = time.strftime("%Y%m%d%H%M", time.localtime())
		# mysql默认数据库
		self.sys_dbs = ("mysql", "information_schema", "test", "performance_schema", "sys")

		# 完成连接数据库并备份
		self.connect_db()
		self.dump_db()

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
		except:
			print("[ %s ] 连接失败，未备份！" % self.servername)
			self.connected = False
			exit()
		# 创建游标
		cursor = self.db.cursor()

		return cursor

	def dump_cmd(self, db_name, badkup_filename):
		"""备份的命令"""
		print("正在备份 %s.%s ……" % (self.servername, db_name))
		os.system(
			"""
			{mysqldump} -u{username} -p{password} -h {host} {db_name} | gzip > {badkup_filename}.gz
			""".format(
					mysqldump=self.mysqldump,
					username=self.username,
					password=self.password,
					host=self.host,
					db_name=db_name,
					badkup_filename=badkup_filename,
					)
		)


	def dump_db(self):
		"""备份所有数据库"""
		# 执行命令，取得命令结果，得到所有数据库
		cur = self.connect_db()
		cur.execute("show databases")
		databases = cur.fetchall()  # 格式为每个库名一个tuple组成的一个tuple

		# 为服务器创建一个单独的文件夹存放备份
		backup_dir0 = self.backup_dir + self.servername + '/'
		if not os.path.exists(backup_dir0):
			os.makedirs(backup_dir0)
		# 备份所有用户数据库
		for row in databases:
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
		"测试服": ("47.244.112.18", "root", r"V%I#QodimTF6fEv7"),
		"Mikey钱包": ("47.75.135.38", "root", r"pKOtbQvYt2vI2K@"),
		"Rtoken钱包": ("47.75.168.170", "root", r"pKOtbQvYt2vI2K@"),
		"ASTC_ECC公链钱包": ("rm-j6c5cmwm82rg5l04qao.mysql.rds.aliyuncs.com", "mikey", r"LjeH8xOJwbLs09"),
		"畅优购商城": ("47.96.79.197", "root", r"ev^m8WdBY#3!JUPy"),
		#"ASTC浏览器": ("47.244.52.38", "root", r"PhzQS4vpYgyo"),
		"链友": ("47.52.157.173", "root", r"iv2VE85$^3WT"),
		"链客财经": ("47.75.128.230", 'root', r"HwFJUjgtB6q5Z^o8"),
		"Wsex交易所": ("rm-j6ck250e5kzzok579io.mysql.rds.aliyuncs.com", "dbuser", r"KZ6U8%rej*nM5Ocu"),
		"交易所_newp": ("47.244.18.129", "root", r"1Qa9O6p1n^@xnD6yjR"),
		"dht钱包": ("47.52.228.139", "root", r"souzbGOpy&fTmNv&", 6336),
	}



	for key,value in hosts.items():
		BackupDB(key, value)

