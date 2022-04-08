# BirthdayAutomator
A bot that uses Selenium and Python3 to ensure you never miss sending another "Happy Birthday!" message on Facebook again.

# Dependencies
1. Python3 (https://www.python.org/downloads/)
2. Selenium (https://pypi.org/project/selenium/)
3. ChromeDriver (https://chromedriver.chromium.org/downloads)

# Setup
Setup requires you to edit 'bot.py' and configure your username and password. Please note, that storing hardcoded credentials presents a potential security risk. Store and execute this script from a directory with permissions restricted to your user account.

Additionally, you will need to utilize a scheduling service to run the script daily.

For Windows, this means creating a scheduled task that executes this script. (https://datatofish.com/python-script-windows-scheduler/)
For Linux, you will need to create a cronjob. (https://www.geeksforgeeks.org/how-to-schedule-python-scripts-as-cron-jobs-with-crontab/)
