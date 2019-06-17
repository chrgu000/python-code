#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functions import BackupDB

hosts = {
    "db-mikey钱包": ("103.112.211.147", "root", r"Cy1NaFG7JnIQgdkt", 5336),
    "db-astc_ECC公链钱包": ("uv2wp8olmf.zzcdb.dnstoo.com", "astcdb", r"Q2eEhoPX7wBH1MTk"),
    "db_摩氪头条": ("172.31.234.4", "root", r"HwFJUjgtB6q5Z^o8"),
    "测试服务器": ("172.31.233.253", "root", r"V%I#QodimTF6fEv7"),
}



for key,value in hosts.items():
    b = BackupDB(key, value)
    if b.connected:  # 连接成功后开始备份，失败则跳过当前数据库
        b.mysqldump = "/usr/bin/mysqldump"
        b.backup_dir = '/data/db_backup/'
        #print(b.mysqldump)
        b.dump_db()
