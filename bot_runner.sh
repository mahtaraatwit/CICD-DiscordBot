#!/bin/bash

sudo crontab -l > cron_bkp
*/5 * * * * /Discord/ping.sh >/dev/null 2>&1 >> cron_bkp
sudo crontab cron_bkp
sudo rm cron_bkp

pipenv shell
pipenv run python launcher.py