import configparser
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver
from bs4 import BeautifulSoup

class Application:
    def __init__(self) -> None: 
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.config = config['AUTHENTIFICATION']
        
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = undetected_chromedriver.Chrome(options=options)
        self.driver.start_session()
        self.login()


    def get_list(self, name) -> dict:
        data = dict()
        
        self.driver.get('https://nnmclub.to/forum/tracker.php')
        self.driver.find_element(By.ID, 'nm').send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@value='Поиск']").click()

        site = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = site.find_all('a', class_='genmed topictitle', href=True)
        
        for line in results:
            data[line.string] = line.attrs["href"]

        return data


    def get_item(self, url) -> None:
        self.driver.get('https://nnmclub.to/forum/' + url)
        self.driver.find_element(By.LINK_TEXT, 'Скачать').click()
        sleep(5)


    def login(self) -> None:
        login_url = 'https://nnmclub.to/forum/login.php'
        self.driver.get(login_url)
        
        while self.driver.page_source.count('Cloudflare'):
            sleep(1)
        
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.config.get('login'))
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.config.get('password'))
        self.driver.find_element(by=By.NAME, value='login').click()
        
        while self.driver.page_source.count('Введите ваше имя и пароль для входа в систему'):
            sleep(1)