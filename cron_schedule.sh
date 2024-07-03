#!/bin/sh

/home/singhnavneet.su/console-access-automation/venv/bin/python3.9 /home/singhnavneet.su/console-access-automation/main.py

# */3 * * * * /home/singhnavneet.su/console-access-automation/cron_schedule.sh >> /home/singhnavneet.su/console-access-automation/cron.log 2>&1