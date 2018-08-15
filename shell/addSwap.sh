#!/usr/bin/env bash
# 添加swap分区脚本，默认8G，文件位于/data目录下，修改完后需要独立修改/etc/fstab文件
# 这个脚本是根据UCloud整理的基本命令
# 使用的目录是/data
free -m
dd if=/dev/zero of=/data/swapfile bs=1M count=8192
chmod 600 /data/swapfile
mkswap /data/swapfile
swapoff -a
swapon /data/swapfile
free -m
