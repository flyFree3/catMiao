#!/bin/bash
if [ -d $1 ]
then
	rm -rf $1
	mkdir $1
else
	mkdir $1
fi


for (( i=1;i<=$1;i++ ))
do
	echo $i
	echo "echo $i $2" > ./$1/$i.sh
done
chmod -R 755 *
