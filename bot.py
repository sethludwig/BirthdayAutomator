#!/usr/bin/python3
"""Main module."""
import secrets
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Config
LOGIN_PAGE = "https://m.facebook.com/"
BIRTHDAYS_PAGE = "https://m.facebook.com/events/birthdays/"
USERNAME = ""
PASSWD = ""

# Functions
def generate_info(message_type,message):
    """Generates a timestamp and outputs a structured console information line."""
    timestamp = datetime.now().isoformat(timespec='seconds')
    print("["+timestamp+"]["+message_type+"] "+message)

def generate_useragent():
    """Used to generate a useragent string. Normally create some sort of config file
    and parse it with a random line read, but not necessary here."""
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/99.0.4844.84 Safari/537.36"
    return useragent

def login_action(driver):
    """Logs in to Facebook."""
    email = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
        '//*[@id="m_login_email"]')))
    password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
        '//*[@id="m_login_password"]')))
    email.send_keys(USERNAME)
    password.send_keys(PASSWD)
    password.submit()

def send_message(driver):
    """Checks for named elements in the response, uses sendkeys and iterates through each.
    Submits random birthday message."""
    messages = ["Happy birthday!", "Hope you have an awesome birthday!",
    "Wishing you a very happy birthday!", "Another 365 days around the sun, congrats!"]
    birthday_input = driver.find_elements(By.NAME,'message')
    generate_info("INFORMATION", "Processing todays birthdays, and recent birthdays.")

    for row in birthday_input:
        try:
            message = secrets.choice(messages)
            row.send_keys(message)
        except:
            generate_info("WARNING", "No birthdays today, or you already wished happy birthday to\
 this user.")
        finally:
            row.submit()
    generate_info("INFORMATION", "Sent birthday wishes.")

def create_driver():
    """Creates the Chrome webdriver for Selenium."""
    useragent = generate_useragent()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--user-agent=%s' % useragent)
    return webdriver.Chrome(options=chrome_options)

def startup():
    """Where the magic happens."""
    generate_info("INFORMATION", "Started program.")
    try:
        driver = create_driver()
        driver.get(LOGIN_PAGE)
        login_action(driver)
        generate_info("INFORMATION", "Logged in as '"+USERNAME+"'.")

        driver.get(BIRTHDAYS_PAGE)
        generate_info("INFORMATION", "Retrieved birthday events page.")
        send_message(driver)

    except WebDriverException:
        pass
    except:
        traceback.print_exc()
    finally:
        driver.quit()
        generate_info("INFORMATION", "Program finished.")

if __name__ == '__main__':
    try:
        startup()
    except:
        print ("Error: Unable to start program.")
