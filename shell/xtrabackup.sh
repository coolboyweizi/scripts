#!/usr/bin/sh
# @desc: percona备份脚本。需要使用percona-xtrabackup


# mysql用户
user=root
# mysql密码
password=

# 备份时间戳
backup_date=`date +%y%m%d-%H%M`

# mysql配置文件
mysql_conf_file=/etc/my.cnf
# 备份项目目录
backup_pre=/data/backup/mysql
# backup目录
backup_dir=$backup_pre/data
# 备份生成日志目录
log_dir=$backup_pre/log
# 生成压缩包路径
zip_dir=$backup_pre/zip

#percona-xtrabackup 备份软件路径
xtrabackup_dir=/usr/local/percona-xtrabackup

# 创建对应的文件夹
mkdir -p $backup_dir
mkdir -p $log_dir
mkdir -p $zip_dir

# 备份文件夹名
backup_folder=${backup_date}

mkdir -p $backup_dir/$backup_folder
if [ $? -ne 0 ]; then
        echo "创建目录文件夹异常"
        exit 1
fi

# 检查备份脚本是否可执行
if [ ! test -x ${xtrabackup_dir}/bin/innobackupex ];then
    echo "xtrabackup_dir没有找到可执行文件innobackupex"
    exit 1
fi

# 全量备份
function full_backup() {
    $xtrabackup_dir/bin/innobackupex \
            --defaults-file=$mysql_conf_file \
            --user=$user \
            --password=$password \
            --no-timestamp \
            $backup_dir/$backup_folder > $log_dir/${backup_folder}.log 2>&1

    if [ $? -ne 0 ]; then
        echo "全量备份错误"
        exit 1
    fi
}

# 打包
function zip_backup() {
    /usr/bin/tar -cjf $zip_dir/$backup_folder.tar.bz2 $backup_dir/$backup_folder > \
          $log_dir/${backup_folder}.tar.log 2>&1
    if [ $? -ne 0 ]; then
        echo "打包备份文件错误"
        exit 1
    fi
}

full_backup
zip_backup


# 删除data目录。
rm -rf $backup_dir

# 删除3天前日志文件
find $backup_pre -type f -mtime +3 -exec rm {} \;

# 删除7天前的压缩文件
find $zip_dir -type f  -mtime +7 -exec rm {} \;
