#!/usr/bin/bash
# Desc: 从其他服务器下载日志


destdir=/data/log/bak/openresty
basedir=/data/log/openresty
m=`date +%m`
y=`date +%Y`
d=`date +%d`
localdir=/tmp/log
realfile=$destdir/$y/$m/$y$m$d\_api.sing.plus.access.log

function download()
{
  echo $1
  scp $1:$realfile $localdir/$1
}


rm -rf $localdir
mkdir -p $localdir
# 下载
download fr-app
download fr-app-s1
#download fr-app-s2


awk '{$1="fr-app"}1' $localdir/fr-app >> $localdir/log
awk '{$1="fr-app-s1"}1' $localdir/fr-app-s1 >> $localdir/log
#awk '{$1="fr-app-s2"}1' $localdir/fr-app-s2 >> $localdir/log

python data.py 6 30 < $localdir/log | python sendmail.py
