#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from db_backup import BackupDB

hosts = {
    "db-mikey钱包": ("103.112.211.147", "root", r"Cy1NaFG7JnIQgdkt", 5336),
    "db-astc_ECC公链钱包": ("uv2wp8olmf.zzcdb.dnstoo.com", "astcdb", r"Q2eEhoPX7wBH1MTk")
}



for key,value in hosts.items():
    back = BackupDB(key, value)
    back.mysqldump = "/usr/bin/mysqldump"
    back.backup_dir = '/oss_hk/db_backup/'
    #print(back.mysqldump)
    back.dump_db()