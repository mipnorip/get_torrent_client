import configparser
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver

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
        result = {}
        return result


    def get_items(self, path) -> None:
        pass


    def login(self):
        login_url = 'https://nnmclub.to/forum/login.php'
        self.driver.get(login_url)
        
        while self.driver.page_source.count('Cloudflare'):
            sleep(1)
        
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.config.get('login'))
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.config.get('password'))
        self.driver.find_element(by=By.NAME, value='login').click()
        
        while self.driver.page_source.count('Введите ваше имя и пароль для входа в систему'):
            sleep(1)
        
        self.driver.close()
        self.driver.quit()