#!usr/bin/bash

while true
do
	git pull
	git add .
	git commit -m 'auto commit'
	git push origin
	sleep 400
done
