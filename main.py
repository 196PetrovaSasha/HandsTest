from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_phone_numbers(url):
    driver = webdriver.Chrome()
    driver.get(url)

    buttons = driver.find_elements(By.TAG_NAME, 'button')

    phone_numbers = []

    for button in buttons:
        if button.is_displayed() and button.is_enabled():
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable(button))
            button.click()
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            text = soup.get_text()
            numbers = re.findall(
                r'(\+7[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}|\d{1}\d{3}\d{3}\d{2}\d{2}|8[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2})',
                text)
            phone_numbers.extend(numbers)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    text = soup.get_text()
    numbers = re.findall(
        r'(\+7[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}|\d{1}\d{3}\d{3}\d{2}\d{2}|8[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2})',
        text)
    phone_numbers.extend(numbers)

    driver.quit()
    return phone_numbers


urls = ['https://hands.ru/company/about', 'https://repetitors.info', 'https://hlebnasushny.ru']

for url in urls:
    print(url)
    phone_numbers = find_phone_numbers(url)
    for number in phone_numbers:
        print(number)



# import requests
# from bs4 import BeautifulSoup
# import re

# def find_phone_numbers(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     text = soup.get_text()
#     numbers = re.findall(
#       r'(\+7[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}|\d{1}\d{3}\d{3}\d{2}\d{2}|8[\-\s]?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2})',
#       text)
#     return phone_numbers

# urls = ['https://hands.ru/company/about', 'https://repetitors.info']

# for url in urls:
#     phone_numbers = find_phone_numbers(url)
#     for number in phone_numbers:
#         print(number)
