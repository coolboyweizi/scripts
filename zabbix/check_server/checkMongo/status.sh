#!/bin/env bash
##mongo_status.sh##
case $# in
 3)
  output=$(/bin/echo "db.serverStatus().$3" |mongo $1:$2/admin -u repl_admin -p 'netdog()MongoR#' --quiet)
  ;;
 4)
  output=$(/bin/echo "db.serverStatus().$3.$4" |mongo $1:$2/admin -u repl_admin -p 'netdog()MongoR#' --quiet)
  ;;
 5)
  output=$(/bin/echo "db.serverStatus().$3.$4.$5" |mongo $1:$2/admin -u repl_admin -p 'netdog()MongoR#' --quiet)
  ;;
esac
if [[ "$output" =~ "NumberLong"  ]];then
 echo $output|sed -n 's/NumberLong(//p'|sed -n 's/)//p'
else
 echo $output
fi