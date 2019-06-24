#!/bin/sh
# Auto format and mount first disk on /data

disk_new=`cat /proc/partitions | grep ".*db$" | awk '{print $4}'`
# aliyun ECS disk is vda..vdb……
if [ $disk_new  -a ! -e "/dev/${disk_new}1" ]; then
fdisk /dev/${disk_new} << EOF
n
p
1


wq
EOF

# format
mkfs.ext4 /dev/${disk_new}1

# mount to /data
mkdir /data
mount /dev/${disk_new}1 /data

# auto mount disk onboot
echo "/dev/${disk_new}1 /data   ext4    defaults        0 0" >> /etc/fstab
fi

# chang sshd port

PORT=7221
if [ ${1} ] ;then
    if [ "$1" -gt 1024 -a "$1" -lt 65535 ] 2>/dev/null; then
	PORT=$1
    fi
fi

if ! grep -n "^Port" /etc/ssh/sshd_config > /dev/null;then
    sed -i "s/^#Port.*$/Port ${PORT}/" /etc/ssh/sshd_config
fi
firewall-cmd --zone=public --add-port=7221/tcp --permanent
firewall-cmd --reload
systemctl restart sshd

echo "=========================================="
echo -e "\033[36m[ `df -Th | grep $disk_new | awk '{print $1, " ",  $7}'` ]\033[0m"
echo "=========================================="
echo -e "\033[36mSSHd [ `grep -n "^Port.*" /etc/ssh/sshd_config | cut -d ":" -f 2` ]\033[0m"