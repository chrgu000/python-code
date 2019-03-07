#!/bin/sh
# Auto format and mount first disk on /data

# aliyun ECS disk is vda..vdb……
if [ -e "/dev/vdb" ]; then
fdisk /dev/vdb << EOF
n
p
1


wq
EOF

# format
mkfs.ext4 /dev/vdb1

# mount to /data
mkdir /data
mount /dev/vdb1 /data

# auto mount disk onboot
echo "/dev/vdb1	/data	ext4	defaults	0 0" >> /etc/fstab
fi

# chang sshd port
sed -i '18i\Port 6221' /etc/ssh/sshd_config
systemctl restart sshd
