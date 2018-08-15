#!/usr/bin/bash
# @desc: flume 的日志整理，用于singplus的notification
# @usage:  任务计划确执行

# 目标文件目录
destination=/data/log/flume/api_notification/
# 源文件目录
source=/data/go_projects_runtime/api.sing.plus/storage/logs/
# 日期
currentDay=`date -d yesterday +%Y-%m-%d`
# 根据日期获得文件
currentFile=notification-${currentDay}.log

if [ ! -f "${source}${currentFile}" ];then
    # 源文件不存在则不执行
    echo "${source}${currentFile} is not found"
elif [ -f "${destination}${currentFile}" ];then
    # 文件存在。跳过
    echo "${currentFile} has done"
else
    echo "${currentFile} is copying"
    cp ${source}${currentFile} ${destination}
fi