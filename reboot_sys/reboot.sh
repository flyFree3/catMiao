#!/bin/bash
workpath=`pwd`
cd $workpath
source config.ini
let times=$(($times+1))
dateTime=$(date "+%Y-%m-%d %H:%M:%S")
echo "$dateTime reboot times:$times" >> $workpath/reboot.log
sed -i "2c times=$times" config.ini
number=$end
if [ $times -le $number ];then
	sleep 30
	reboot
fi
