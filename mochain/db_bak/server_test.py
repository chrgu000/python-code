#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from db_backup import BackupDB

hosts = {
    "db-localhost": ("47.244.112.18", "root", r"V%I#QodimTF6fEv7"),
}


for key,value in hosts.items():
    back = BackupDB(key, value)
    back.mysqldump = "/usr/bin/mysqldump"
    back.backup_dir = '/data/backup/'
    #print(back.mysqldump)
    back.dump_db()