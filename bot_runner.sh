#!/bin/bash

sudo crontab -l > cron_bkp
sudo echo "*/5 * * * * /Discord/ping.sh >/dev/null 2>&1" >> cron_bkp
sudo crontab cron_bkp
sudo rm cron_bkp

kill -9 $(ps -A | grep python | awk '{print $1}')

pipenv shell
pipenv run python launcher.py
exit 0