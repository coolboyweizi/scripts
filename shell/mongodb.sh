#!/usr/bin/bash
# @desc:  mongodb 备份脚本
# usage:  mongodb.sh mongodb://localhost:27017 dbname username password
backup_dat=`date +%F`
backup_pre='/data/backup/mongodb'
backup_dir=${backup_pre}/${backup_dat}
backup_zip=${backup_pre}/zip



mongodump='/usr/local/mongodb-3.4.4/bin/mongodump '

mongohost=$1    # 主机地址，mongodb://host:port
mongodbs=$2     # mongo数据库
mongouser=$3    # 用户验证
mongopwd=$4     # 密码验证

if [ $# -ne 4 ]; then
    echo "usage : ${0} mongohost dbname username password"
    exit 1
fi

#创建目录
mkdir -p ${backup_dir}
if [ $? -ne 0 ]; then
    echo "备份目录${backup_dir}发生异常"
    exit 1
fi

# 开始备份
echo 'start dump'
${mongodump} -h ${mongohost} -o ${backup_dir} -d ${mongodbs} -u "${mongouser}" -p "${mongopwd}" --authenticationDatabase admin
if [ $? -ne 0 ]; then
    echo "备份发生异常错误"
    exit
fi

# 进行打包
cd ${backup_pre} && tar -cjf ${backup_dat}.tar.bz2 ${backup_dir}
if [ $? -ne 0 ]; then
    echo "打包发生异常错误"
    exit
fi

# 删除data目录
rm -rf $backup_dir

# 删除3天前日志文件
find $backup_pre -type f -mtime +3 -exec rm {} \;

# 删除7天前的压缩文件
find $zip_dir -type f  -mtime +7 -exec rm {} \;
