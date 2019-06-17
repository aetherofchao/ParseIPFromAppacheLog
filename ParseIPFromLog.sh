#!/bin/bash

# adressa access logu; redhad, debian
LOG_PATHS="/var/log/httpd/access_log,/var/log/apache2/access.log,/var/log/apache/access.log"

if  [ $# -gt 0 ];then

	mkdir /tmp/LogAccessFiles12345


	scp $@:\{$LOG_PATHS\} /tmp/LogAccessFiles12345

	# protože technicky stahujeme několik souborů naráz nemůžeme access log pojmenovat
	for log in /tmp/LogAccessFiles12345/* ;do

		# 1. stahnout acces log
		mv $log ./access.log
	done

	# clean
	rm -rf /tmp/LogAccessFiles12345

	python pythonscript.py

else
	echo Usaga: ./ParseIPFromLog.sh  [-346BCpqrv] [-c cipher] [-F ssh_config]
	echo "			   "[-i identity_file] [-l limit] [-o ssh_option] 
	echo "			   "[-P port] [-S program] 
	echo "			   "[user@hostname]
fi