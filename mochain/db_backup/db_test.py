#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functions import BackupDB

hosts = {

    "测试服务器": ("cs.mochain.co", "root", r"V%I#QodimTF6fEv7"),
}

users = ['apphost', 'pms', 'test','root']

for key,value in hosts.items():
    b = BackupDB(key, value)
    if b.connected:  # 连接成功后开始备份，失败则跳过当前数据库
        #b.mysqldump = "/usr/bin/mysqldump"
        #b.backup_dir = '/data/db_backup/'
        #print(b.mysqldump)
        #b.dump_db()
        db = b.db
        # 创建游标
        cur = db.cursor()
        # 执行命令
        for username in users:
            cur.execute("select host, user from mysql.user where user=\"{}\"".format(username))
            # 读取内容
            #result = cur.fetchall()
            #print(result)
            for x in cur.fetchall():
                print("""用户名：{0[1]:<16s}\t主机：{0[0]}""".format(x))